# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


BEAMER = True


root = Path(__file__).parent.parent

plt.style.use("ggplot")

if BEAMER:
    with plt.xkcd():
        fig, axes = plt.subplots(1, 2, dpi=200, figsize=(9, 3.2))
    font = {"size": 11}
else:
    plt.rc("text", usetex=True)
    fig, axes = plt.subplots(2, 1, dpi=200, figsize=(3.5, 6))
    font = {"size": 8}

ax1, ax2 = axes.ravel()

km = 1.5
k1 = np.logspace(0, km, dtype=float, endpoint=True)
k2 = np.logspace(km, 4, dtype=float, endpoint=True)
c = "k-"
km = 10 ** km
coef = km ** (-6.7 / 5)

print("coef =", coef)
ax1.set_title("Energy spectra predicted by Kraichnan's theory", fontsize=font["size"] + 1)
ax1.loglog(k1, k1 ** -(5 / 3) * coef, c)
ax1.loglog(k2, k2 ** (-3), c)

ax2.set_title("Observed atmospheric energy spectra", fontsize=font["size"] + 1)
ax2.loglog(k2, k2 ** (-5 / 3) * coef, c)
ax2.loglog(k1, k1 ** -3, c)

ax1.annotate(
    r"Forcing, $P=\epsilon+\eta$",
    (km, km ** -3),
    (km, km ** -1.5),
    arrowprops=dict(
        #  arrowstyle="fancy",
        shrink=0.05,
        # posB=(km, km ** -1.5)
    ),
    ha="left",
    fontsize=font["size"],
)
ax1.text(
    0.1*km, (0.8*km)**(-5/3),
    r"$\epsilon^{2/3}k^{-5/3}$",
    fontdict=font,
)
ax1.text(
    100*km, (80*km)**-3,
    r"$\eta^{2/3}k^{-3}$",
    fontdict=font,
)
ax2.text(
    0.1*km, (0.08*km)**(-3),
    r"$k^{-3}$",
    fontdict=font,
)
ax2.text(
    100*km, (800*km)**-(5/3),
    r"$k^{-5/3}$",
    fontdict=font,
)


def arrow(ax, x, y, arrowroot=0.1, exp=-3):
    return ax.annotate(
        "",
        (x*km, (y*km)**exp),
        (x*arrowroot*km, (y*arrowroot*km)**exp),
        arrowprops=dict(
            arrowstyle='fancy',
            #  shrink=0.15,
        ),
        #  ha="left",
    )

arrow(ax1, 0.1, 0.8, 6, -5/3)
arrow(ax1, 100, 80)

for ax in ax1, ax2:
    #  ax.get_xaxis().set_ticks([])
    #  ax.get_yaxis().set_ticks([])
    ax.get_xaxis().set_ticklabels([])
    ax.get_yaxis().set_ticklabels([])
    ax.set_ylabel(r"$E(k)$")
    ax.set_xlabel(r"$k$")
    #  ax.get_xaxis().set_visible(False)
    #  ax.get_yaxis().set_visible(False)

fig.tight_layout()
# plt.show()


if BEAMER:
    fig.savefig(root / "cascade_horiz.png")
else:
    fig.savefig(root / "cascade.pdf")
