
import matplotlib.pyplot as plt

from util import show, save

from fluiddyn.output.rcparams import set_rcparams

from fluidcoriolis.carriage.oscillate import calcul_oscillate_movement

set_rcparams(fontsize=20, for_article=True)

times, speeds, positions = calcul_oscillate_movement(
    V=0.08, L=7.0, x_a=0.25, nb_periods=3)

fig = plt.figure()
ax = fig.gca()

ax.plot(positions, times)

tmax = times.max()
tmin = times.min()
ax.plot([-2.75, -2.75], [tmin, tmax], ':k')
ax.plot([2.75, 2.75], [tmin, tmax], ':k')

ax.set_xlabel('$x_c$ (m)')
ax.set_ylabel('$t$ (s)')

fig.tight_layout()

save(fig, 'fig_movement_carriage.png')

show()
