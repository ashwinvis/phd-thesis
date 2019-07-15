# Software stack

This project also an exercise in developing an reproducible, open-source
workflow. This was motivated by the fact that experiments in fluid mechanics
typically rely on a combination of proprietary software which includes: bundled image
processing software by vendors such as Dantec and LaVision, virtual
instrumentation development platform Lab View and a collection of Matlab
utilities. Since most laboratories have invested in developing expertise in
such software, the easier approach would have been to reuse existing tools.
However, this model is restrictive and cannot be transformed into a
reproducible and collaborative workflow. Furthermore, since this project
involves terabytes of image data, there was a clear need for scalable image
processing framework which is not inhibited by license restrictions, which to
the best of our knowledge did not exist. Hence a path off the beaten track was
pursued during the course of MILESTONE project to develop three software
package and apply them into the project.

## FluidLab: a generic API for laboratory devices

## FluidCoriolis: utilities for calibrating and conducting experiments

## FluidImage: a scalable image processing framework

* libre: no license required to run on HPC clusters
* asynchronous processing: massive parallelization
* single tooling for entire post-experiment workflow: calibration,
  preprocessing, PIV, postprocessing of velocity fields
* limitations: algorithms

