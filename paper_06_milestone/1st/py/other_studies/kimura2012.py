
import numpy as np

label = r'Kimura at al. (2012, $\sim 1024^3$)'
symbol = 'bo'

N2 = np.array([1., 10, 50, 100])
N = np.sqrt(N2)

Lb = np.array([1.7406e-1, 5.6729e-2, 2.9586e-2, 2.0633e-2])

U = Lb*N

lo = np.array([7.2357e-2, 1.2598e-2, 4.1222e-3, 2.3432e-3])
eta = np.array([1.5070e-3, 1.5230e-3, 1.4560e-3, 1.4891e-3])

epsK = lo**2*N**3

nu = (eta**4*epsK)**(1./3)

Rt = epsK/(nu*N**2)

Fht = epsK/(U**2*N)
