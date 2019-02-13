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

keys_outplace = (
    'fortran',
    'numpy',
    'pythran',
    'pythran\nloops',
    'numba\nloops'
)

# on my KTH laptop
times_outplace = np.array([22.1, 66.6, 36.2, 19.1, 24.4,])
times_inplace = np.array([9., 54.2, 18.3, 8.5, 14.6,])

# on my LEGI desktop with g++
times_outplace = np.array([25.6, 74.2, 41.0, 23.0, 28.7,])
times_inplace = np.array([7.3, 56.2, 17.5, 7.64, 14.7,])

# on my LEGI desktop with clang 6.0
times_outplace = np.array([25.6, 74.2, 41.0, 22.3, 28.7,])
times_inplace = np.array([7.3, 56.2, 17.4, 7.19, 14.7,])

left = [0, 1, 2, 3, 4]

colors = ('w', 'y', 'c', 'c', 'b')

fig, axes = plt.subplots(2, figsize=(8, 4))

for ax in axes:
    ax.set_ylim(0, 78)

ax = axes[0]

ax.bar(left, height=times_outplace, color=colors, edgecolor='k', yerr=2)

ax.set_xticks([])
ax.set_xticklabels([])
ax.set_ylabel('elapsed time (ms)')
ax.set_title('out-of-place (with memory allocation)')

xlim = ax.get_xlim()
ax.plot(xlim, (times_outplace[0],)*2, 'k:')
ax.set_xlim(xlim)

y = 55
for x, s in zip(left, keys_outplace):
    ax.text(x, y, s, rotation=20,
            horizontalalignment='center',
            verticalalignment='center')

keys_inplace = (
    'fortran',
    'numpy',
    'pythran',
    'pythran\nloops',
    'numba\nloops')

colors = ('w', 'y', 'c', 'c', 'b')

left = np.arange(len(times_inplace)) + len(times_outplace)

ax = axes[1]

ax.bar(left, height=times_inplace, color=colors, edgecolor='k', yerr=2)

ax.set_xticks([])
ax.set_xticklabels([])
ax.set_ylabel('elapsed time (ms)')
ax.set_title('in-place')

xlim = ax.get_xlim()
ax.plot(xlim, (times_inplace[0],)*2, 'k:')
ax.set_xlim(xlim)

y = 45
for x, s in zip(left, keys_inplace):
    ax.text(x, y, s, rotation=20,
            horizontalalignment='center',
            verticalalignment='center')

fig.tight_layout()

path_fig = os.path.join(here_tmp, 'fig_microbench.pdf')

if 'save' in sys.argv:
    fig.savefig(path_fig, dpi=800)
else:
    plt.show()
