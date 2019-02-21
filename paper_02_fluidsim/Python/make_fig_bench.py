#!/usr/bin/env python

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

import bench_analysis as ba
from base import matplotlib_rc
from sync import path_fluidsim_bench_results


matplotlib_rc()
save = True
root = Path(path_fluidsim_bench_results) / 'benchmarks'
# pattern2d = root.glob('beskow_1024x1024')
pattern2d = sorted(root.glob('beskow_?0??x????'))
pattern3d = sorted(root.glob('beskow_*x*x*'))[::-1]


def increase_lims(ax, fac=2):
    fac = np.array([1/fac, fac])
    xlim = np.array(ax.get_xlim()) * fac
    ylim = np.array(ax.get_ylim()) * fac
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)


def plot_fig(pattern, solver, output_file=None, exclude=[]):
    fig, axes = plt.subplots(1, 2)
    ax0, ax1 = axes.ravel()
    markers = ("x", ".")
    for ipath, path_dir in enumerate(pattern):
        t_min = 1e10
        path_dir = str(path_dir)
        N = path_dir.rpartition("_")[-1].split("x")
        N = [int(n) for n in N]
        fig, t_min = ba.plot_scaling(
            path_dir, solver, 'any', *N,
            show=False, type_plot='strong', fig=fig, ax0=ax0, ax1=ax1,
            t_min_cum=t_min, default_marker=markers[ipath],
            type_fft_exclude=exclude)

    ax0.set_title('')
    ax0.set_ylabel(r'$S$')
    ax0.set_xlabel(r'$n_p$')
    ax1.set_ylabel(r'Walltime per iteration (s)')
    ax1.set_xlabel(r'$n_p$')

    increase_lims(ax0)
    increase_lims(ax1)
    fig.set_size_inches(6, 3)
    fig.suptitle('')
    fig.tight_layout(
        pad=1.02, h_pad=None, w_pad=None, rect=(-0.01, -0.02, 1, 1)
    )
    if output_file is None or not save:
        plt.show()
    else:
        fig.savefig(output_file)

    return fig, axes


plot_fig(pattern2d, 'ns2d', '../tmp/fig_bench_strong2d.pdf', [])
plot_fig(pattern3d, 'ns3d', '../tmp/fig_bench_strong3d.pdf', ["pfft", "fftw1d"])
