from util import show, save

import numpy as np
import matplotlib.pyplot as plt

g = 9.81
rho_min = 1.0
N = 0.5
H = 0.8

l_nomixed = 0.35

zs = np.linspace(0, H, 40) - H
zmid = H / 2

# approximation...
dz_rho = -N ** 2 * rho_min / g
rhos = rho_min + dz_rho * zs

rho0 = rho_min - dz_rho * zmid
rhos1 = rho0 + l_nomixed * dz_rho * np.tanh((zs + zmid) / l_nomixed)

z0 = np.trapz(rhos * zs, zs) / np.trapz(rhos, zs)
z1 = np.trapz(rhos1 * zs, zs) / np.trapz(rhos1, zs)

rho_max = rhos.max()
rho_min = rhos.min()

fig = plt.figure(figsize=(8, 3.5))
ax0 = fig.add_subplot(121)
ax1 = fig.add_subplot(122)

ax0.set_title("initial condition (linear strat.)", {"color": "b"})
ax1.set_title("effect of mixing", {"color": "r"})

axes = [ax0, ax1]

ax0.plot(rhos, zs, "b")
# ax0.plot([rho_min, rho_max], [z0]*2, 'b')
# ax0.plot([rho_min, rho_max], [-zmid]*2, 'k:')


def addtext(ax, z, color):
    ax.text(
        1.005,
        -0.6,
        "center of mass\n" + f"{1000*z:.1f} mm",
        {"size": 14.0, "color": color, "horizontalalignment": "center"},
    )


addtext(ax0, z0, "b")

ax1.plot(rhos, zs, "b:")
ax1.plot(rhos1, zs, "r")
# ax1.plot([rho_min, rho_max], [z1]*2, 'r')
# ax1.plot([rho_min, rho_max], [-zmid]*2, 'k:')

addtext(ax1, z1, "r")

for ax in axes:
    ax.set_xlabel(r"$\bar\rho(z)$ (kg/l)")
    ax.set_ylabel(r"$z$ (m)")

fig.tight_layout(pad=0.2, w_pad=1.0)

save(fig, "fig_scheme_mixing.png")
show()
