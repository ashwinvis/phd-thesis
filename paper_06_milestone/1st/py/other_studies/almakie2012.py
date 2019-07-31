
import numpy as np

label = r'Almakie et al. (2012, $\sim 4096^2\times 1024$)'
symbol = 'go'

epsK = np.array([0.87, 0.64, 0.64])

epsKh = np.array([0.58, 0.43, 0.44])

Eh = np.array([1.56, 1.54, 1.74])

Uh = np.sqrt(Eh)

F4 = np.array([0.0615, 0.0231, 0.0105])

Fht = F4*epsK/epsKh

Rt = np.array([222.6, 40.62, 10.19])

Ret = Rt/Fht**2

nu = Eh**2/(epsK*Ret)

N = epsKh/(F4*Eh)

ko = np.sqrt(N**3/epsK)

kd = (epsK/nu**3)**(1./4)

nh = 4096
Lh = 2*np.pi
Delta = Lh/nh
C_dealiasing = 2./3
kmax = C_dealiasing*np.pi*nh/Lh

kb = N/Uh
