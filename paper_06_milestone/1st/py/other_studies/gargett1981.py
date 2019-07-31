

import numpy as np

label = 'Gargett et al. (1981, ocean)'
symbol = 'rv'

# N (rad/s)
N = np.array([3.94e-3, 3.96e-3, 4.59e-3])

# epsK (cm^2 s^{-3})
epsK = np.array([7.4e-6, 1.4e-5, 3.9e-5])
epsK *= 1e-4 # (m^2 s^{-3})

# ko (rad/m)
ko0 = np.array([9.1, 6.7, 5.0])

# Phib = sqrt(epsK*N) (s^{-2} m^{-1})
Phib0 = np.array([1.7e-6, 2.3e-6, 4.2e-6])  

Phib = np.sqrt(epsK*N)

ko = np.sqrt(N**3/epsK)

nu = 1.1e-6  # (m^2/s)

Rt = epsK/(nu*N**2)

kb = np.array([0.18351, 0.17514, 0.22024])

Uh = N / kb

Eh = Uh**2

Fht = epsK / (N * Eh)
