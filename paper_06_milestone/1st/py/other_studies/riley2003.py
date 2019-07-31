
import numpy as np

label = 'Riley et al. (2003, $\sim 512^3$)'
symbol = 'mo'

F = 4.
N = 2 * np.pi / F

Re_l = np.array([1600., 3200, 6400])
nu = 1./Re_l

epsK = 3.e-3 * np.ones_like(Re_l)
E = 0.06

Fht = epsK / (N * E)

Rt = epsK / (nu * N**2)
