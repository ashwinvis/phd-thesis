---
figPrefix: figure
---
In the recent years, there has been a call to reform the way we perform
scientific research. This includes improving _findability, accessibility,
interoperabilty_ and _reusability_ of research data, otherwise known as FAIR
principles [@wilkinson_fair_2016]. This also allows for increased scrutiny and
transparency in research results.

MILESTONE project has therefore strived to make the project data openly
available for everyone. The raw data which includes images and signals from
density and temperature probes collectively amounts to several terabytes.
Although solutions exist to share slices of very large datasets
[@cornillon_opendap_2003], the utility of the such data is limited without
post-processing. Upon post-processing the total size of the data has been
condensed to less than four gigabytes. A possible solution to share datasets of
the order of few gigabytes is to upload them in general-purpose repositories
such as Zenodo [@peters_zenodo_2017]. In this way, the dataset would be
_findable_ via a date of issue identifier or the search interface of Zenodo,
and _accessible_ for downloading through standard internet protocols. The
dataset consists of HDF5 and XML files, which includes metadata describing
experimental parameters. Use of descriptive and standardised data formats
allows for _interoperability_ and _reuse_ in other research software.

Results are deemed reproducible, when the source code used to operate on the
data are accessible [@peng_reproducible_2011]. Therefore, a set of
open-source packages programmed using Python were used to conduct a good
majority of the tasks. The packages are now part of the FluidDyn project
[@fluiddyn]. The code used to postprocess and analyse the data are archived in
a package called `fluidcoriolis`. The package can be reused in the future, to
load and interact with the data. Additionally the package contains scripts
which were used to conduct the experiments and perform image processing using
packages `fluidlab` and `fluidimage` respectively.

The package `fluidlab` is designed as a generic API for orchestrating
laboratory experiments. An experiment in the simplest level can be thought of
as a network of interconnected instruments awaiting commands and also sending
and receiving data. For example, the movement of the carriage and of the
probes are controlled with a graphical application and scripts provided
by `fluidlab` and `fluidcoriolis`. Horizontal scanning PIV is also made
possible by controlling the rotating mirror and the triggers of the camera
through functions provided in `fluidlab`. This allows anyone to replicate, a
horizontal scanning PIV setup with a good camera (in this case, _pco.edge_), a
rotating mirror and an inexpensive acquisition board (_T7 LabJack_) to trigger
the camera.

The computation of PIV is performed on the cluster at LEGI using `fluidimage`.
The development of `fluidimage` [@augier_fluidimage_2016] as a scalable image
processing framework, is one of the biggest undertakings during the project.
Free software for processing PIV such as UVMAT [@sommeria_uvmat_2008] is a
source of inspiration behind this project. UVMAT offers a graphical interface
built on MATLAB, which gives valuable interactive experience while setting
parameters for PIV.  However, to process terabytes of image data, there is a
clear need for a scalable image processing framework. Limited availability of
MATLAB licenses inhibits scalability of UVMAT in high performance clusters.
This led to the development of `fluidimage` and its current capabilities
include,

* asynchronous processing which allows massive parallelization, and

* single tooling for all sorts of post-experiment workflows, including
  calibration, preprocessing, PIV, post-processing of velocity fields.

![A flowchart describing PIV computation in `fluidimage`. The oval blocks
signify a _work_ and the rectangles are the _queues_. The black arrows
represent which are handled by the main thread, and are classified as _global_.
A _global_ work can be invoked once (_one shot_) or many times (_multiple
shots_). I/O bound and CPU bound _works_ are shown in green and orange
respectively. Image and velocity arrays are shown as small blue and purple
squares inside the _queues_.](./imgs/topology_piv.pdf){#fig:topopiv
width=40% height=60%}

Parallelization in `fluidimage` is achieved by dividing a workflow into several
tasks called _works_. To allow the flow of data from one _work_ to another,
which operate at various speeds, intermediate data structures called _queues_
are created. If a _work_ is fast enough, it is handled by the main thread.
Slower _works_ are parallelized depending on the kind of operations involved.
As shown in @fig:topopiv, image file names are read and grouped in the form of
couples by the main thread. Images are read as arrays using several threads.
Thereafter based on the couples of names, couples of arrays are formed and
through FFT based cross-correlation, the velocity field is computed. Saving
velocity fields into the disk is also handled by a multithreaded _work_. The
package also includes _topologies_ for preprocessing images with filters. Other
features of `fluidimage` include ability to calibrate cameras using camera
models of @tsai_versatile_1987 and @zhang_flexible_2000, and a
postprocessing module for extracting statistics from computed velocity fields.
