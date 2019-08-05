"""Make the figure fig_Gamma_vs_Fh.png

Uses at least

/fsnet/project/coriolis/2016/16MILESTONE/Data_post/PCO_top/Energy_budget/fit_exp73.h5
"""
from util import plt, show, save

year = 2016

assert year in (2016, 2017)

if year == 2016:
    from fluidcoriolis.milestone.results_energy_budget import ResultEnergyBudgetExp
elif year == 2017:
    from fluidcoriolis.milestone17.results_energy_budget import ResultEnergyBudgetExp

extract = True

if year == 2016:
    cam = 'PCO_top'
    iexp = 39  # good for the document
    iexp = 73  # good for the document

    # iexp = 18  # horrible eps
    # iexp = 22  # quite wrong
    # iexp = 21  # horrible
    # iexp = 24  # eps too large
    # iexp = 64  # bad eps
    # iexp = 34  # bad eps?
    # iexp = 72  # not great...
    # iexp = 69
    # iexp = 66
else:
    # Milestone17
    cam = 'Cam_horiz'
    iexp = 19


results = ResultEnergyBudgetExp(iexp, cam, extract=extract)
exp = results.exp
eps = results.eps
fit = results.fit
Uc = fit.Uc
time = fit.time
time1 = fit.time1
time2 = fit.time2
kens = fit.kens
kenfit1b = fit.kenfit1b
kenfit1bm = fit.kenfit1bm
kenfit1bM = fit.kenfit1bM
kenfit2 = fit.kenfit2

abs_dt_E = fit.dtkenfit1_v2v + fit.v2vs
epsm = fit.dtkenfit1_v2v
epsmfit11b = fit.epsfit11b
epsmfit11bm = fit.epsfit11bm
epsmfit11bM = fit.epsfit11bM

fig, (ax, ax1) = plt.subplots(nrows=2)

ax.plot(time, kens/Uc**2, 'b', label='raw data')
ax.plot(time1, kenfit1b/Uc**2, 'r', label='fit')
ax.plot(time1, kenfit1bm/Uc**2, 'b', label='fit')
ax.plot(time1, kenfit1bM/Uc**2, 'b', label='fit')

ax.set_xlabel(r'$(t-t_0)/T$')
ax.set_ylabel(r'$E_K/U_c^2$')

ax.set_xscale('log')
ax.set_yscale('log')

ax = ax1

norm = exp.epsc
# ax.plot(time2, abs_dt_E/norm, 'b', label='raw data')
ax.plot(time2, epsm/norm, 'g', label='fit - v2v')
ax.plot(time1, epsmfit11b/norm, 'r', label='fit')
ax.plot(time1, epsmfit11bm/norm, 'b', label='fit')
ax.plot(time1, epsmfit11bM/norm, 'b', label='fit')

ax.set_xlabel(r'$(t-t_0)/T$')
ax.set_ylabel(r'$\varepsilon_m / \varepsilon_c$')

ax.set_xscale('log')
ax.set_yscale('log')

if iexp in [39, 73]:
    ax.set_ylim([1e-4, 1.2e-2])

fig.tight_layout()

save(fig, 'fig_fit_EK.png')

show()
