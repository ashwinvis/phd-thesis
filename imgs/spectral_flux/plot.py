import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection
from math import pi
import numpy as np
from pathlib import Path

root = Path(__file__).absolute().parent.parent

plt.style.use("seaborn-paper")

matplotlib.rcParams['text.latex.preamble'] = [r"\usepackage{amsmath}"]
plt.rc('text', usetex=True)
plt.rc('figure', dpi=300)

SIDE_TEXT = False

if SIDE_TEXT:
    fig = plt.figure(figsize=(10,5))
    fig.subplots_adjust(right=5/10)
    ax = fig.add_subplot(111)
else:
    fig, ax = plt.subplots(figsize=(5,5))

circle1 = Circle((0, 0), pi/2)
circle2 = Circle((0, 0), pi/1.9)
circle3 = Circle((0, 0), pi * 2)
patches = [circle3, circle2, circle1]

p = PatchCollection(patches, cmap="Pastel1")#, alpha=0.4)
#  colors = np.array([54, 50, 20])
p.set_array(np.array([0.1, 2, 9]))
#  p.set_cmap(cmap)
ax.add_collection(p)

arror_r = pi / 2**1.5
ax.arrow(arror_r, arror_r, 0.3, 0.3, head_width=0.05, head_length=0.1, fc='k', ec='k')
tex = r"$\Pi(\mathbf{k}, t) = \sum\limits_{|\mathbf{k'}| \geq |\mathbf{k}|} T(\mathbf{k}', t)$"
ax.text(0.9, 1.2, tex, fontsize=15, va='bottom', rotation=45)

if SIDE_TEXT:
    tex = '\n'.join([
        r'$T=T_K + T_A$',
        r'$T_K=-\frac{1}{2}ik_i(\hat{u_j}\widehat{u_iu_j}^* - \hat{u_j}^*\widehat{u_iu_j})$',
        r'$T_A=-\frac{1}{2}ik_i(\hat{\phi}\widehat{u_i \phi}^* - \hat{\phi}^*\widehat{u_i\phi})$'
    ])
    ax.text(pi + 0.2, pi/2, tex, fontsize=20)

    tex = r'''$\Pi=\Pi_K + \Pi_A$
    $\Pi=\Pi_{VVV} + \Pi_{VVW} + \Pi_{VWW} + \Pi_{WWW}$'''

    ax.text(pi + 0.2, pi/4, tex, fontsize=20)
ax.set_xlabel(r'$k_x$', fontsize=15)
ax.set_ylabel(r'$k_y$', fontsize=15)
ax.set_ylim(0, pi)
ax.set_xlim(0, pi)
# plt.show()
fig.tight_layout()
fig.savefig(root / "spectral_flux.pdf")
