
# Comparison with the Fortran 90 code ns3d (https://bitbucket.org/paugier/ns3d)

ns3d is a highly efficient code (MPI + OpenMP, but I don't use OpenMP in these
benchmarks). It has been highly optimized by so generations of PhD students so
it is really fast. However, it is limited to 2d decomposition for the 3d FFT.

## 2d case

~/Dev/fluidsim/bench/profiling$ python simul_profile_ns2d.py
~/Dev/ns3d/jobs$ ./job_bench2d_seq.py

fluidsim.solvers.ns2d is 15 % faster than ns3d in 2d (case 1152x1152, in
sequential and with MPI with 4 processes). ns3d in 2d (which has been used for
real studies and articles) does too many FFTs. However, the FFT from fluidfft
are significantly slower than the 2d fft from ns3d. We should be able to at
least decrease this difference. 

## 3d case

~/Dev/fluidsim/bench/profiling$ python simul_profile_ns3d.py
~/Dev/ns3d/jobs$ ./job_bench3d_seq.py

fluidsim.solvers.ns3d is 15 % slower than ns3d for a shape 128x128x128 (in
sequential and with MPI with 4 processes). It is mainly due to slower FFTs (25%
slower).

ns3d is highly optimized for the 3d case. It uses inplace FFTs with padding
(and good flags). It's really fast. We still have to understand why we are
slower with fluidfft.

Note that 15% slower than a highly optimized and specialized Fortran code is
not so bad. And we just need to be better in FFTs and the difference between
the 2 codes will become negligible. Note that this is what is going to happen
for very large simulations for which MPI communication take more time.

What we see:

- The time spent in Python is really negligible. We see that we don't loose
  time in Python, but in C++ code (FFT)!

- Pythran can lead to very fast computational kernels (really as fast than the
  Fortran's one). To get these results, it has been necessary to write the
  loops explicitly (see fluidfft/fft3d/util_pythran.py).

- To optimize a solver, it is important to avoid memory allocations and memory
  copies.

- For very large case, we can use pfft and p3dfft while it is not possible with
  ns3d.

- I'd like to test using FFT with Cuda. Cyrille, does it work? Can you show me
  how to try this at LEGI?
