"""Make the figure fig_R_vs_Fh.png

"""

import numpy as np

from util import plt, get_colors, show, save

from fluidcoriolis.milestone17.results_energy_budget import ResultEnergyBudgetExp

iexps = list(np.r_[15:22, 23, 24])
iexps.remove(18)  # inconsistent result (?)
iexps.remove(19)  # inconsistent result (?)

colors = get_colors(len(iexps))

fig = plt.figure(figsize=(9, 8))

rect = [0.1, 0.08, 0.56, 0.5]
ax0 = fig.add_axes(rect)

rect = [0.1, 0.67, 0.38, 0.31]
ax1 = fig.add_axes(rect)

rect[0] = 0.6
ax2 = fig.add_axes(rect)

axes = [ax0, ax1, ax2]

xlim = [3e-3, 0.1]
ylim = [1e-1, 2e2]

Flim = 3e-2
Rlim = 10
color = [0.9] * 3
linewidth = 20
ax0.plot([Flim] * 2, [Rlim, ylim[1]], "-", color=color, linewidth=linewidth)
ax0.plot(xlim, [Rlim] * 2, "-", color=color, linewidth=linewidth)


print(iexps)

for i, iexp in enumerate(iexps):
    print("\niexp = ", iexp)
    results = ResultEnergyBudgetExp(iexp, "Cam_horiz", extract=True)

    exp = results.exp
    if exp.N == 0.8:
        symbol = "o"
    elif exp.N == 0.56:
        symbol = "s"
    else:
        symbol = "v"
    ax0.plot(
        results.Fht,
        results.Rt,
        symbol,
        color=colors[i],
        label=r"exp {}, $N =$ {:.2f} rad/s, $U_c =$ {:.0f} cm/s".format(
            iexp, exp.N, 100 * exp.Uc
        ),
    )

    if ~np.isnan(results.Fht):
        ax0.text(results.Fht, results.Rt, str(iexps[i]), fontsize=8)
        ax1.errorbar(
            results.Fht,
            results.eps / exp.epsc,
            yerr=results.deltaeps / exp.epsc,
            fmt=symbol,
            ecolor=colors[i],
        )
        # ax1.plot(results.Fht, results.eps / exp.epsc, symbol, color=colors[i])
        # ax2.plot(results.Fht, (results.urms / exp.Uc)**2, symbol, color=colors[i])
        ax2.errorbar(
            results.Fht,
            results.ken / (exp.Uc ** 2),
            yerr=results.deltaken / (exp.Uc ** 2),
            fmt=symbol,
            ecolor=colors[i],
        )
ax0.set_xlabel(r"$F_h$")
ax0.set_ylabel(r"$\mathcal{R}$")

ax1.set_xlabel(r"$F_h$")
ax1.set_ylabel(r"$\varepsilon_m / ({U_c}^3/D_c)$")

ax2.set_xlabel(r"$F_h$")
ax2.set_ylabel(r"$E_{Kh} / U_c^2$")

for ax in axes:
    ax.set_xscale("log")
    ax.set_yscale("log")
    # ax.set_xlim(xlim)

# ax0.set_ylim(ylim)
# ax2.set_ylim([0.01, 0.1])

ax2.set_yticklabels([], minor=True)

ax0.legend(loc=(1.02, 0.0), fontsize=10, numpoints=1)

# fig.tight_layout()

save(fig, "fig_R_vs_Fh_2017.png")
show()
