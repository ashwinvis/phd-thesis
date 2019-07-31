
from util import show, save

import numpy as np
import matplotlib.pyplot as plt

from fluidcoriolis.milestone17.time_signals import SignalsExperiment, comments

from fluidcoriolis.milestone17.exp import iexps_strat, create_exp

nu = 1e-6

C_eps = 2e-3
C_E = 4e-2

C_eps = 3e-3
C_E = 4e-2

"""

eps_K = C_eps * Uc**3 / Dc

E_K = C_E * Uc**2


"""


iexps = [iexp for iexp in iexps_strat
         if iexp in comments and comments[iexp].startswith('ok')]

iexps_bad = (
    24,  # too mixed at the beginning
    57, 58,  # horizontal cylinders
    15,  # not long enough
)


iexps = [iexp for iexp in iexps if iexp not in iexps_bad]

print(iexps)

exps = [create_exp(iexp) for iexp in iexps]

exps = [exp for exp in exps if exp.Uc > 0.01]

signals_exps = [SignalsExperiment(exp) for exp in exps]

dt_energies = np.zeros([len(exps)])
Fhs = np.zeros_like(dt_energies)
Ds = np.zeros_like(dt_energies)
Rs = np.zeros_like(dt_energies)
for i, signals in enumerate(signals_exps):
    _, _, _, _, _, dt_e = signals.calcul_energy_pot_vs_time()

    dt_energies[i] = dt_e/C_eps
    Fhs[i] = C_eps/C_E*signals.exp.Fhc
    Ds[i] = signals.exp.Dc
    Rs[i] = C_eps * signals.exp.epsc / (nu * signals.exp.N**2)

fig = plt.figure(figsize=(9, 5))
ax = fig.gca()

plot = ax.scatter

cond = Ds == 0.25
plot(Fhs[cond], dt_energies[cond], c=Rs[cond], marker='o', vmin=0, vmax=20)

cond = Ds == 0.5
sc = plot(Fhs[cond], dt_energies[cond], c=Rs[cond], marker='s', vmin=0, vmax=20)

for i, exp in enumerate(exps):
    ax.text(Fhs[i], dt_energies[i], str(exp.iexp), size=12)

xs = np.linspace(3e-2, 9e-2, 10)
ax.plot(xs, 3e-2 * xs**-1, "k")
ax.text(5e-2, 6.5e-1, r"${F_h}^{-1}$")

xs = np.linspace(0.1, 0.15, 10)
ax.plot(xs, 3e-3 * xs**-2, "k")
ax.text(0.12, 2.5e-1, r"${F_h}^{-2}$")

ax.set_xlabel(r'$F_h$')
ax.set_ylabel(r'dimensionless $\varepsilon_P$')

fig.text(0.85, 0.05, r'$\mathcal{R}$', size=20)

ax.set_xscale('log')
ax.set_yscale('log')

plt.colorbar(sc)

fig.tight_layout()

# for s in signals_exps:
#     s.plot_energy_pot_vs_time()

save(fig, 'fig_dt_pot_energy.png')
show()
