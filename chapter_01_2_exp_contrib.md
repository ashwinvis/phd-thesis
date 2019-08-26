# Software systems

The project was also an exercise in developing a reproducible, open-source
workflow. This was motivated by the fact that experiments in fluid mechanics
typically rely on a combination of proprietary software which includes: bundled
image processing software by vendors such as Dantec[^d] and LaVision[^la], virtual
instrumentation development environment LabVIEW[^lv] and a collection of MATLAB
Utilities. The most obvious advantage of such software is that these
have been developed over several years and have advanced capabilities. Since most
laboratories have invested in developing expertise in such software, the most
conventional approach would have been to reuse existing tools.
However, such an approach is restrictive and cannot be transformed into a
reproducible and collaborative workflow, for example making use of a version
control systems. Algorithms are not entirely transparent and the closed-source
nature prevents customizations.  Hence a path off the beaten track was pursued
during the course of MILESTONE project to make use of three open-source
software packages, extend them to meet the project goals and use them for
executing the project. We will now look at the capabilities of the packages
that were used.

[^d]: [https://www.dantecdynamics.com/particle-image-velocimetry](https://www.dantecdynamics.com/particle-image-velocimetry)
[^la]: [https://www.lavision.de/en/techniques/piv-ptv](https://www.lavision.de/en/techniques/piv-ptv)
[^lv]: [http://www.ni.com/en-us/shop/labview.html](http://www.ni.com/sv-se/shop/labview.html)

## Fluidlab

The package `fluidlab` was designed as a generic API for orchestrating
laboratory experiments. The software leverages the object-oriented programming
features in Python to model real life instrumentation. An experiment in the
simplest level can be thought of as a network of interconnected instruments
awaiting commands and also sending and receiving data. Being one of the oldest
packages within the FluidDyn project [@fluiddyn], prior to the commencement of
MILESTONE, `fluidlab` had this structure in place. Nevertheless, the package had to be
extended to support the hardware used in the experiment. Thus,
the team involved in the MILESTONE project developed software for controlling
the motors of the carriage, for calibrating and data acquisition with
conductometric probes.

## Fluidimage

The development of `fluidimage` [@augier_fluidimage_2016] as a scalable image
processing framework, was one of the biggest undertaking during MILESTONE. Free
software for processing PIV such as UVMAT [@sommeria_uvmat_2008] was a source
of inspiration behind this project. UVMAT offers a GUI built on
MATLAB, which gives valuable interactive experience while setting parameters
for PIV. However, license restrictions and the GUI-first design inhibits
scalability of its execution in high performance clusters.  Furthermore, since
the MILESTONE project involves terabytes of image data, there was a clear need for
a scalable image processing framework. This was a collaborative effort and the
work involved was divided between the group of developers. The following design
goals guided the development of `fluidimage`:

* asynchronous processing which allows massive parallelization,
* single tooling for all sorts of post-experiment workflows, including calibration,
  preprocessing, PIV, post-processing of velocity fields.


Parallelism for a image-processing framework is perhaps the most attractive
feature of `fluidimage`. This was implemented using _data_ or _task
parallelism_ for time consuming operations. Any such particular workflow can be
regarded as a set of data arrays undergoing a series of operations, of which
the slow operations are parallelized. Slow operations are either CPU bound or
input/output (I/O) bound. As the name suggests, I/O bound operations do not
require heavy computation and are limited
by storage or memory read/write access speed. Python's standard library support
multithreading, which are lightweight in terms of memory and useful for I/O
bound tasks. For CPU bound tasks we need to spawning multiple processes, which
do not share memory but can execute different cores of the CPU at the same
time[^gil].
<!-- The code can process keeping multiple threads alive at the same time -->
<!-- (concurrent) but only one one thread would be given instruction at a particular -->
<!-- time (not parallel). Since I/O instructions take some time in fulfilling the -->
<!-- task, the thread involved can be put to "sleep" for a brief amount of time. -->
For programming with threads there are a handful of standard libraries
(`threading, concurrent.futures` and `asyncio`) to choose from which contains
the essential building blocks.  Earlier versions of `fluidimage` used
`threading` which had a low-level abstraction and difficulties such as threads
refusing to stop when errors are encountered.  Now, `fluidimage` manages
threads using a library called `trio` which ensures that threads are
well-behaved [@smith_notes_2018; @smith_trio_2017].  CPU bound operations are
executed using the standard library `multiprocessing`. These are implemented
within a module `fluidimage.executors`.

[^gil]: See chapter 3 of the thesis, where we discuss this restriction which is called a
      Global Interpreter Lock (GIL).


<div id="fig:topologies">
![Topology for PIV `fluidimage.topologies.piv`](./imgs/topology_piv.pdf){#fig:topopiv width=44%}
![Topology for image preprocessing, `fluidimage.topologies.preproc`](./imgs/topology_preproc.pdf){#fig:topopre width=49%}

_Topologies_ for asynchronous task parallelism in `fluidimage`. The oval blocks
signify a _work_ and the rectangles are the _queues_. The black arrows
represent which are handled by the main thread, and are classified as _global_.
A _global_ work can be invoked once (_one shot_) or many times (_multiple
shots_). I/O bound and CPU bound _works_ are shown in green and orange
respectively. Image and velocity arrays are shown as small blue and purple
squares inside the _queues_.
</div>

A workflow, from disk to disk, consisting of several tasks are conceptualized
into classes termed _topologies_.  A task in `fluidimage` terminology is called
a _work_. Some examples of a _work_ are PIV using FFT or cross-correlation, or
preprocessing the image with a median filter or a global minimum intensity
threshold to remove noise.  To allow the flow of data from one _work_ to
another, which operate at various speeds, we have intermediate data structures
called _queues_. A _queue_ can be assigned an upper limit on the number of
arrays it can store, and whenever this count is below the limit a _work_ would
be assigned to fill the _queue_ and delete the array from the preceding
_queue_. If a _work_ is fast enough, it is handled by the main thread. As shown
in @fig:topopiv image names are read and grouped in the form of couples by the
main thread as preparation.  Reading images as arrays in to the memory is done
using several threads. Thereafter these arrays are associated with the couple
of names and through cross-correlation or FFT, the velocity field is computed.
Saving velocity fields into the disk is also handled by a multithreaded _work_.

One of my key contribution in `fluidimage` was to adapt the PIV topology for
preprocessing the images, as shown in @fig:topopre. The _queues_ were inherited
and modified such that, instead of accepting a couple of data allows for more
number of data arrays.  Also the image processing functions in the libraries
`scikit-image`, `scipy.ndimage`, and `OpenCV` were unified form a preprocessing
_toolbox_, `fluidimage.preproc` -- a module filled with functions which either
accept a single array or a handful of arrays, along with preprocessing
parameters to yield the results. Multiple image-processing could be invoked in
succession within a single _topology_.

To achieve the second goal of unifying the workflow, some efficient operations
were implemented in Python within `fluidimage`. This means that it can leverage
mathematical operations from mature third party packages or written clearly
using Python's expressive syntax. Being a young project, a limited
set of algorithms were implemented initially, such as 2D-2C planar PIV,
stereographic reconstruction for 2D-3C PIV, simple 2D camera calibration and
camera calibration algorithm of @tsai_versatile_1987 which also accounts for
image distortion. Part of the camera calibration workflow relied on the
graphical interface of UVMAT to identify the image coordinates of the
calibration target.

The package continues to grow in features exceeding the scope of MILESTONE
project. In 2018, a set of modules were added to `fluidimage` to automate
calibration using OpenCV [@bradski_learning_2008], which automatically detects
grid points of a calibration target[^cv] and implements the camera model by
@zhang_flexible_2000. A tomographic reconstruction [@atkinson_efficient_2009]
module was added which implements multiplicative line of sight (MLOS)
algorithm[^tomo].

[^cv]: https://fluidimage.readthedocs.io/en/latest/ipynb/tuto_opencv_calibration.html
[^tomo]: https://fluidimage.readthedocs.io/en/latest/ipynb/tuto_opencv_tomo_reconstruct.html

## Fluidcoriolis

![GUI provided by
`fluidcoriolis` for controlling
carriage](./imgs/MILESTONE/fluidcoriolis.jpg){#fig:fluidcoriolis width=80%}

Since `fluidlab` was intended to be a library, several details specific to the
requirements of MILESTONE were separately developed into a package called
`fluidcoriolis`, named after the experimental facility.
The package `fluidcoriolis` is composed of a graphical user interface shown in
@fig:fluidcoriolis to operate the carriage, calibrate the probes were constructed by
utilizing the `fluidlab` API. Scripts to launch pre-processing, PIV and
post-processing using `fluidimage` was also included in this package. To
organize and interact with the processed data, a thin API using a class
`fluidcoriolis.milestone.exp.Experiment` was also created.

