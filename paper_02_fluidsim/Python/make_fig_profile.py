#!/usr/bin/env python
import os
import getpass
from pathlib import Path

import matplotlib.pyplot as plt

from fluidsim.util.console import profile as pf
from fluiddyn.util import modification_date

from base import matplotlib_rc, titles, curdir


save = True
force_make = False  # ; force_make = True
matplotlib_rc() if save else matplotlib_rc(dpi=150)
textprops = dict(fontsize=10, family="monospace")
figx = 5    # 9  # 20 / 2.54
figy = 2.1  # 2  # 6 / 2.54

root = Path("/tmp") / getpass.getuser() / "fluidsim-bench-results" / "profiles"
if not os.path.exists(str(root)):
    raise FileNotFoundError("Run sync.py")

patterns2d = [
    (root / "beskow_1024x1024/").glob("*np=1_*fftw2d*"),
    (root / "beskow_1024x1024/").glob("*np=8*fftwmpi2d*"),
]

patterns3d = [
    (root / "beskow_128x128x128/").glob("*np=1_*fftw3d*"),
    (root / "beskow_128x128x128/").glob("*np=8*fftwmpi3d*"),
    (root / "beskow_512x512x512/").glob("*np=2_*fftwmpi3d*"),
    (root / "beskow_512x512x512/").glob("*np=128*fftwmpi3d*"),
    # (root / 'beskow_1024x1024x1024/').glob('*np=1024*p3dfft*'),
    # (root / 'beskow_1024x1024x1024/').glob('*np=1024*fftwmpi3d*'),
]


def paths_from_patterns(patterns):
    try:
        path_stats = [str(next(p)) for p in patterns]
    except StopIteration:
        raise ValueError("Bad glob pattern or path does not exist.")

    return path_stats


paths2d = paths_from_patterns(patterns2d)
paths3d = paths_from_patterns(patterns3d)


def plot(path, ax, title="", **kwargs):
    path_dir = os.path.dirname(path)
    nb_dim = path_dir.split("_")[1].count("x") + 1
    times, long_functions = pf.analyze_stats(path, nb_dim)

    color_map = plt.get_cmap("Pastel1")
    num_of_colors = len(long_functions) + 1
    colors = color_map([x / num_of_colors for x in range(num_of_colors)])

    patches, texts, autotexts = pf.plot_pie(
        times,
        long_functions,
        ax,
        times_descending=True,
        for_latex=True,
        startangle=0,
        explode=0.5,
        textprops=textprops,
        counterclock=False,
        pctdistance=0.8,
        colors=colors,
        **kwargs
    )
    ax.set_title(title, loc="left", size=12)


def modif_title(title, path, with_resolution=True):
    resol, nb_proc = path.split("_np=")
    resol = resol.rsplit("_", 1)[-1]
    nb_proc = nb_proc.split("_", 1)[0]
    resol = resol.replace("x", r"$\times$")
    if with_resolution:
        title += " " + resol + ","
    title += " " + nb_proc + " process"
    if int(nb_proc) > 1:
        title += "es"
    return title


modif_date_input_2d = min(modification_date(path) for path in paths2d)
modif_date_input_3d = min(modification_date(path) for path in paths3d)

path_fig = curdir + "/../tmp/fig_profile{}.pdf"
path_fig2d = path_fig.format("2d")
path_fig3d = path_fig.format("3d")

if Path(path_fig2d).exists():
    modif_date_fig_2d = modification_date(path_fig2d)
    has_to_make2d = modif_date_fig_2d < modif_date_input_2d
else:
    has_to_make2d = True

if Path(path_fig3d).exists():
    modif_date_fig_3d = modification_date(path_fig3d)
    has_to_make3d = modif_date_fig_3d < modif_date_input_3d
else:
    has_to_make3d = True

if force_make:
    has_to_make2d = True
    has_to_make3d = True

if has_to_make2d:
    pies2d = []
    nrows = 1
    ncols = 2
    fig2d, axes2d = plt.subplots(nrows, ncols)
    for path, ax, title in zip(paths2d, axes2d.ravel(), titles):
        title = modif_title(title, path, with_resolution=False)
        pies2d.append(plot(path, ax, title))  # labeldistance=0.))

    fig2d.set_size_inches(figx * ncols, figy * nrows)
    fig2d.tight_layout()

    if save:
        fig2d.savefig(path_fig2d)

if has_to_make3d:
    pies3d = []
    nrows = 2
    ncols = 2
    fig3d, axes3d = plt.subplots(nrows, ncols)
    for path, ax, title in zip(paths3d, axes3d.ravel(), titles):
        title = modif_title(title, path)
        pies3d.append(plot(path, ax, title))

    fig3d.set_size_inches(figx * ncols, figy * nrows)
    # fig3d.tight_layout()
    fig3d.tight_layout(rect=(-0.01, 0, 0.96, 1))
    # fig3d.subplots_adjust(0.0, -0.02, 0.95, 0.95, wspace=0, hspace=0.2)

    if save:
        fig3d.savefig(path_fig3d)

if not save and (has_to_make2d or has_to_make3d):
    plt.show()
