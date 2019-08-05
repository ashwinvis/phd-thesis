
from util import plt, show, save

cam = 'PCO_top'  # MILESTONE16

year = 2017

assert year in (2016, 2017)

if year == 2016:
    from fluidcoriolis.milestone.results_energy_budget import ResultEnergyBudgetExp
elif year == 2017:
    from fluidcoriolis.milestone17.results_energy_budget import ResultEnergyBudgetExp

if year == 2016:
    cam = 'PCO_top'
    iexp = 73
else:
    cam = 'Cam_horiz'
    iexp = 18

r = ResultEnergyBudgetExp(iexp, camera=cam)

r.plot_energy_vs_time()
fig = plt.gcf()
fig.tight_layout()

save(fig, 'fig_energy_vs_time.png')
show()
