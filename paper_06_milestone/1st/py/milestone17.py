
import os
import sys

import numpy as np
import matplotlib.pyplot as plt

from fluiddyn.output.rcparams import set_rcparams
from fluidcoriolis.milestone.util import get_colors

from fluidcoriolis.carriage.oscillate import calcul_period_oscillate

path_tmp = os.path.join(os.path.split(os.path.split(__file__)[0])[0], 'tmp')
if not os.path.exists(path_tmp):
    os.makedirs(path_tmp)

H = 0.8
nu = 1e-6
alpha_m = 0.1
La = 0.25

C_b = 7e-4
C_eps = 3e-3
C_E = 4e-2


Us = {}
Us[0.25] = np.array([2, 4, 8, 12, 16])*0.01
Us[0.5] = np.array([4, 8, 12, 16, 20])*0.01


def calcul_EN(N, H):
    return (N*H)**2/12


def calcul_mixing_one_period(U, N=0.5, Dc=0.25, L=6):
    return C_b * U**2 / calcul_EN(N, H) * 2 * (L + 2*La)/Dc


def calcul_nt(U, N=0.5, Dc=0.25, L=6):

    mixing1period = calcul_mixing_one_period(U, N, Dc, L)

    t_min = 0.02 / mixing1period
    t_max = 0.1 / mixing1period

    return t_min, t_max


def print_nt(U, N=0.5, Dc=0.25, L=6):
    t_min, t_max = calcul_nt(U, N, Dc, L)
    print('t_min = {} Tc\nt_max = {} Tc'.format(t_min, t_max))


def calcul_nt0(ntmin, ntmax, Tc):

    if ntmax < 1:
        return 0

    if ntmax < 3:
        return 2

    if ntmin < 3:
        return 3

    tmin = ntmin * Tc
    tmax = 3600 * 8

    if tmin > tmax:
        t = tmax
    else:
        t = tmin

    return int(round(t/Tc))


class Exp(object):
    def __init__(self, Uc, Dc=0.25, N=0.55, L=7):
        self.Uc = Uc
        self.Dc = Dc
        self.N = N
        self.L = L

        self.epsc = Uc**3/Dc
        self.eps = C_eps*self.epsc
        self.dt_EPb = C_b*self.epsc
        self.EKh = C_E*Uc**2

        self.Rt = self.eps/(nu * N**2)
        self.Fht = self.eps/(N*self.EKh)
        self.Tc = 2 * (L + 2*La) / Uc

        assert all(calcul_period_oscillate(Uc, L, La) == self.Tc)

        self.mixing_one_period = calcul_mixing_one_period(Uc, N, Dc, L)

        self.t_min, self.t_max = calcul_nt(Uc, N, Dc, L)


label = 'Milestone (2017, exp.)'
symbol = 'r^'

Dc = 0.5
exps = Exp(Us[Dc], Dc=Dc)

Rt = exps.Rt

Fht = exps.Fht

print('Rt', Rt)
print('Ft', Fht)
