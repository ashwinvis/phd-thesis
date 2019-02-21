import os
import sys

import numpy as np
import matplotlib.pyplot as plt

from fluiddyn.output.rcparams import set_rcparams

set_rcparams(fontsize=14, for_article=True, for_beamer=False)

here = os.path.abspath(os.path.dirname(__file__))
here_tmp = os.path.join(here, '../tmp')

if not os.path.exists(here_tmp):
    os.mkdir(here_tmp)

keys = (
    'total',
    'FFT',
    'RK4',
    'curl',
    'vector\nproduct',
    'projection',
)

times_ns3d = np.array([9.52, 6.18, 1.91, 0.49, 0.35, 0.46])
times_fluidsim = np.array([9.45, 6.72, 1.57, 0.44, 0.34, 0.30])
left = 2.2*np.arange(len(times_ns3d))

fig, ax = plt.subplots(1, figsize=(8, 4))

shift = 0.9
ax.bar(left, height=times_ns3d, color='b', edgecolor='k', yerr=0.07)
ax.bar(left+shift, height=times_fluidsim, color='y', edgecolor='k', yerr=0.07)

ax.set_xticks([])
ax.set_xticklabels([])
ax.set_ylabel('time (s)')
# ax.set_title('outplace (with memory allocation)')

y = -0.8
for x, s in zip(left, keys):
    ax.text(x+shift/2, y, s, rotation=0,
            horizontalalignment='center',
            verticalalignment='center')

fig.tight_layout(rect=(0, 0.05, 1, 1))

path_fig = os.path.join(here_tmp, 'fig_compare_with_ns3d.pdf')

if 'save' in sys.argv:
    fig.savefig(path_fig, dpi=800)
else:
    plt.show()
