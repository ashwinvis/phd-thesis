"""Load and plot benchmarks (:mod:`fluidsim.util.console.bench_analysis`)
=========================================================================

"""
import os
from glob import glob
import json
import sys

import pandas as pd
import numpy as np
from scipy.signal import argrelmax, argrelmin, argrelextrema
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from fluidsim.util.console.util import ConsoleError


def load_bench(path_dir, solver, hostname="any"):
    """Load benchmarks results saved as JSON files."""

    dicts = []
    for path in glob(path_dir + "/result_bench_{}*.json".format(solver)):
        with open(path) as f:
            try:
                d = json.load(f)
            except json.decoder.JSONDecodeError:
                print(path)
                raise

        if hostname != "any" and not d["hostname"].startswith(hostname):
            continue

        dicts.append(d)

    df = pd.DataFrame(dicts)
    df = df[df.columns.difference(["pid", "time_as_str"])]
    return df


def filter_by_shape(df, n0, n1, n2=None):
    """Filters all results with the same `n0` and same `n1`."""

    if n2 is None:
        df = df[(df.n0 == n0) & (df.n1 == n1)]
        return df[df.columns.difference(["n0", "n1"])]
    else:
        df = df[(df.n0 == n0) & (df.n1 == n1) & (df.n2 == n2)]
        return df[df.columns.difference(["n0", "n1", "n2"])]


def filter_by_shapeloc(df, n0_loc, n1_loc, n2_loc=None):
    """Filters all results with the same `n0_loc * n1_loc`.

    This implies shapeK_loc has same no. of points. This is a weak check and
    the shapeK_loc may not have the same shape. Make sure all shapes are
    estimated and tested apriori using:

    >>> fluidsim bench -e
    >>> mpirun -np {nb_proc} fluidsim bench -c

    """
    if n2_loc is None:
        df = df[(df.n0_loc * df.n1_loc == n0_loc * n1_loc)]
        return df[df.columns.difference(["n0_loc", "n1_loc"])]
    else:
        df = df[(df.n0_loc * df.n1_loc * df.n2_loc == n0_loc * n1_loc * n2_loc)]
        return df[df.columns.difference(["n0_loc", "n1_loc", "n2_loc"])]


def exit_if_empty(df, input_params):
    """Check if the dataframe is empty."""
    if df.empty:
        print("No benchmarks corresponding to the input parameters:")
        for k, v in input_params.items():
            print(k, "=", repr(v))
        sys.exit()


def plot_scaling(
    path_dir,
    solver,
    hostname,
    n0,
    n1,
    n2=None,
    show=True,
    type_time="usr",
    type_plot="strong",
    fig=None,
    ax0=None,
    ax1=None,
    name_dir=None,
    once=False,
    t_min_cum=1e10,
    default_marker=None,
    type_fft_exclude=[],
):
    """Plot speedup vs number of processes from benchmark results."""

    input_params = dict(
        path_dir=path_dir, solver=solver, hostname=hostname, n0=n0, n1=n1
    )

    if name_dir is None:
        name_dir = os.path.basename(os.path.abspath(path_dir)).replace(
            "_", " "
        ).title()
        name_dir = name_dir.replace("Beskow ", "")

    df = load_bench(path_dir, solver, hostname)
    exit_if_empty(df, input_params)
    df.t_elapsed_sys /= df.nb_iter
    df.t_elapsed_usr /= df.nb_iter

    if type_plot == "strong":
        df_filter = filter_by_shape(df, n0, n1, n2)
    elif type_plot == "weak":
        df_filter = filter_by_shapeloc(df, n0, n1, n2)
    else:
        raise ConsoleError("Unknown plot type.")

    def group_df(df):
        """Group and take median dataframe results with same number of processes.
        """
        # for "scaling" (mpi)
        df = df[df.nb_proc > 1]
        exit_if_empty(df, input_params)

        nb_proc_min = df.nb_proc.min()
        df_grouped = df.groupby(["type_fft", "nb_proc"]).quantile(q=0.2)
        if show:
            print(df)
        return df_grouped, nb_proc_min

    df_filter, nb_proc_min_filter = group_df(df_filter)
    keys_filter = [
        k for k in df_filter.columns if k.startswith("t_elapsed_" + type_time)
    ]

    df_filter = df_filter[keys_filter]
    df_filter_nb_proc_min = df_filter.xs(nb_proc_min_filter, level=1)

    def get_min(df):
        """Get minumum time from the whole dataframe"""
        m = df.as_matrix()
        i0, i1 = np.unravel_index(np.argmin(m), m.shape)
        mymin = m[i0, i1]
        ind = df.index[i0]
        key = df.columns[i1]
        return mymin, ind, key

    t_min_filter, name_min_filter, key_min_filter = get_min(df_filter_nb_proc_min)
    print(
        "{}: Best for {} procs t={} for {}, {}".format(
            path_dir,
            nb_proc_min_filter,
            t_min_filter,
            name_min_filter,
            key_min_filter,
        )
    )

    t_min_filter = min(t_min_filter, t_min_cum)
    # Finally, start preparing figure and plot
    if fig is None or ax0 is None or ax1 is None:
        fig, axes = plt.subplots(1, 2)
        ax0, ax1 = axes.ravel()

    ax0.set_ylabel("speedup ({} scaling)".format(type_plot))
    ax1.set_ylabel("efficiency % ({} scaling)".format(type_plot))

    def plot_once(ax, x, y, linestyle=None, label=None):
        """Avoid plotting the same label again."""
        plotted = any([line.get_label() == label for line in ax.get_lines()])
        color = None
        if linestyle is None:
            if plotted:
                linestyle = [
                    line.get_linestyle()
                    for line in ax.get_lines()
                    if line.get_label() == label
                ][
                    0
                ]
                color = [
                    line.get_color()
                    for line in ax.get_lines()
                    if line.get_label() == label
                ][
                    0
                ]
            else:
                linestyle = "-"

        if not plotted:
            ax.plot(
                x, y, linestyle, label=label, color=color, marker=default_marker
            )
        else:
            ax.plot(x, y, linestyle, color=color, marker=default_marker)

    def add_hline(ax, series=None, y=None):
        """Add a horizontal line to the axis."""
        if y is None:
            y = series.iloc[0]

        xmin = series.index.min()
        xmax = max(series.index.max(), ax.get_xlim()[1])
        # plot_once(ax, [xmin, xmax], [y, y], 'linear')
        ax.plot([xmin, xmax], [y, y], "k-")

    def set_label_scale(ax, xscale="log", yscale="log", basex=2, basey=2):
        """Set log scale, legend and label of the axis."""
        ax.set_xscale(xscale, basex=basex)
        ax.set_yscale(yscale, basey=basey)
        ax.set_xlabel("number of processes")
        # ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    print(df_filter)
    # Plot speedup
    print("Grouped names:")
    for name in df_filter.index.levels[0]:
        tmp = df_filter.loc[name]
        print(name)

        if any([type_fft in name for type_fft in type_fft_exclude]):
            continue
        for k in keys_filter:

            walltime = tmp[k]
            speedup = t_min_filter / walltime * nb_proc_min_filter
            #  if name_dir != "":
            #      label = "{}, {}".format(name.replace("fluidfft.", ""), name_dir)
            #  else:
            label = name.replace("fluidfft.", "")
            label = (label).replace("_", "\_")  # for latex
            label = "{}, {}".format(solver, label)
            label = r'\texttt{' + label + r'}'

            shape_str = "${}^2$" if n2 is None else "${}^3$"
            shape_str = shape_str.format(n0)
            # shape_str = f"{n0}x{n1}" if n2 is None else f"{n0}x{n1}x{n2}"

            # Plot theoretical helper lines
            if type_plot == "strong":
                theoretical = [speedup.index.min(), speedup.index.max()]
                # plot_once(ax0, theoretical, theoretical, 'linear')
                ax0.plot(theoretical, theoretical, "k:", linewidth=1)

                # Plot walltime: theoretical
                theoretical = walltime.values[0] * walltime.index[0] / walltime.index
                ax1.plot(walltime.index, theoretical, "k:", linewidth=1)
                set_label_scale(ax1, "log", "log", basey=10)

                # Plot efficiency: theoretical
                # add_hline(ax1, efficiency, 100)
                # set_label_scale(ax1, 'log', 'linear')
            else:
                add_hline(ax0, speedup, 2)
                add_hline(ax1, walltime, walltime.values[0])

            def text_idx(series):
                # return len(series.index) // 2
                log_series = np.log(series)

                # return int(argrelextrema(log_series, np.less)[0][0])
                try:
                    return int((argrelmin(log_series)[0][0])), 0.8
                except IndexError:
                    return len(series) - 1, 1.2
                    # return np.argmin(np.abs(log_series - np.mean(log_series))), 1.2

            if 'p3dfft' in name or 'fftw1d' in name:
                idx, yfac = text_idx(
                        speedup.values)
                ax0.text(speedup.index[idx] * 1.2, speedup.values[idx] * yfac,
                         shape_str, size=5)
                idx, yfac = text_idx(walltime.values)
                ax1.text(walltime.index[idx] * 1.2, walltime.values[idx] * yfac,
                         shape_str, size=5)
            plot_once(
                ax0, speedup.index, speedup.values, label=label  # default_marker,
            )

            ## Plot walltime
            plot_once(
                ax1,
                walltime.index,
                walltime.values,  # default_marker,
                label=label,
            )

            ## Plot efficiency
            # if type_plot == 'strong':
            #     efficiency = speedup / speedup.index * 100
            # else:
            #     # efficiency = speedup / speedup.iloc[0] * 100
            #     efficiency = speedup / 2 * 100
            # plot_once(ax1,
            #     efficiency.index, efficiency.values,  # 'x-',
            #     # label='{}, {}'.format(name, name_dir))
            #     label=label)



    set_label_scale(ax0)
    ax0.legend(prop=dict(family="monospace"))
    ax0.set_title(
        "Best for {} processes: {}, {}={:.2f} ms".format(
            nb_proc_min_filter,
            name_min_filter,
            key_min_filter,
            t_min_filter * 1000,
        )
    )

    if show:
        plt.show()
    return fig, t_min_filter
