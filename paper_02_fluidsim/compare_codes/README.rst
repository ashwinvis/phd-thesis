Compare pseudo-spectral codes
=============================

Install other codes
-------------------

Script to install and compare similar solvers; viz:

 * spectralDNS
 * dedalus

For these codes, the benchmark scripts are in the directory `fluidsim/bench`.

For ns3d, see https://bitbucket.org/paugier/ns3d (directory `ns3d/jobs`).

Results 2d cases
----------------

Elapsed times in second.

+-------------+---------+----------+
|             |  512^2  |  1024^2  |
+-------------+---------+----------+
|   dedalus   |   8.09  |   43.00  |
+-------------+---------+----------+
| spectralDNS |   0.92  |    3.48  |
+-------------+---------+----------+
|   fluidsim  |   0.51  |    2.65  |
+-------------+---------+----------+
|    ns3d     |   0.82  |    3.96  |
+-------------+---------+----------+

For this case, Dedalus is ~ 30 times slower than fluidsim...

In contrast, the order of magnitude of the elapsed time is similar for the three
other codes.  However, the Fortran code ns3d is surprisingly slow (47% slower than
fluidsim) since there is no specialized numerical scheme for the 2d case in ns3d,
so that more FFTs have to be performed compared to SpectralDNS and fluidsim.
(Even though ns3d has been used for studies based on 2d simulations.)


Results 3d cases
----------------

+-------------+---------+
|             |  128^3  |
+-------------+---------+
| spectralDNS |  11.55  |
+-------------+---------+
|   fluidsim  |   9.45  |
+-------------+---------+
|    ns3d     |   9.52  |
+-------------+---------+

We see that ns3d and fluidsim are basically as efficient for this case. Fluidsim
is even slightly faster! Let's understand this better with a finer comparison
between the results for these two codes.

Fine comparison between fluidsim and ns3d (case 128^3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On my computer at LEGI:

+----------------+---------+----------+
|                |  ns3d   | fluidsim |
+----------------+---------+----------+
|     total      |   9.52  |    9.45  |
+----------------+---------+----------+
|      FFT       |   6.18  |    6.72  |
+----------------+---------+----------+
| time stepping  |   1.91  |    1.57  |
+----------------+---------+----------+
|      curl      |   0.49  |    0.44  |
+----------------+---------+----------+
| vector product |   0.35  |    0.34  |
+----------------+---------+----------+
|  projection    |   0.46  |    0.30  |
+----------------+---------+----------+

On my laptop (pyfftw is slow! 25% slower than ns3d! Linked to the same fftw?):

+----------------+---------+----------+
|                |  ns3d   | fluidsim |
+----------------+---------+----------+
|     total      |  10.63  |   10.91  |
+----------------+---------+----------+
|      FFT       |   6.62  |    8.05  |
+----------------+---------+----------+
| time stepping  |   2.50  |    1.66  |
+----------------+---------+----------+
|      curl      |   0.43  |    0.39  |
+----------------+---------+----------+
| vector product |   0.39  |    0.39  |
+----------------+---------+----------+
|  projection    |   0.39  |    0.34  |
+----------------+---------+----------+

- ns3d's FFT are very fast: the FFT execution is 0.55 s longer for fluidsim
  (nearly 9% longer). This difference is especially important for sequential run
  for which there is no communication cost in the FFT computation.

  This difference can partially be explained by the fact that in ns3d, all FFTs
  are inplace (so the input can be erased during the transform).  Another factor
  is that the flag FFTW_PATIENT is used in ns3d which leads to very long
  initialization and some times faster FFTs. Since we did not see significant
  speed-up by using this flag in fluidsim and that we also care about
  initialization time, this flag is not used and we prefer to use the flag
  FFTW_MEASURE, which usually leads to similar performance.

- ns3d's time stepping is significantly slower than fluidsim's time stepping (0.34
  s = 20 %). We did not find the performance issue in ns3d.

- slightly faster linear operators in fluidsim (thanks to Pythran) + unnecessary
  projections (5 per time step in ns3d compared to 4 per time step in fluidsim).

Although the FFTs are a little bit faster for ns3d, the total time is slightly
smaller (less than 1% of the total time) for fluidsim for this case.

Conclusions
-----------

These examples do not show that fluidsim is always faster than ns3d or as fast as
any very well optimized Fortran codes.  However, we see that our very high-level
and modular Python code is very efficient and is not much slower that a
well-optimized Fortran code.
