
import os
import getpass
from subprocess import call

# import matplotlib.pyplot as plt

from fluiddyn.util import modification_date


here = os.path.abspath(os.path.dirname(__file__))
here_tmp = os.path.join(here, '../tmp')


if not os.path.exists(here_tmp):
    os.mkdir(here_tmp)

path_tmp = os.path.join('/tmp', getpass.getuser())
if not os.path.exists(path_tmp):
    os.mkdir(path_tmp)

repo_fluidsim_bench_results = \
    'https://bitbucket.org/fluiddyn/fluidsim-bench-results'
path_fluidsim_bench_results = os.path.join(path_tmp, 'fluidsim-bench-results')

has_to_pull = True

if os.path.exists(path_fluidsim_bench_results):
    if has_to_pull:
        os.chdir(path_fluidsim_bench_results)
        call(['hg', 'pull', '-u'])
else:
    os.chdir(path_tmp)
    call(['hg', 'clone', repo_fluidsim_bench_results])

os.chdir(here)


# def save_fig_scaling(dir_name, dim, n0, n1, n2=None):
#     path_dir = os.path.join(path_fluidsim_bench_results, dir_name)
#     path_fig = os.path.join(here_tmp, 'fig_' + dir_name + '.pdf')

#     if not os.path.exists(path_fig) or \
#        modification_date(path_dir) > modification_date(path_fig):
#         print('make fig', path_fig)
#         fig = plot_scaling(path_dir, None, dim, n0, n1, n2, show=False,
#                            for_latex=True)
#         fig.set_size_inches(10, 5)
#         fig.suptitle('')
#         fig.tight_layout(
#             pad=1.02, h_pad=None, w_pad=None, rect=(-0.01, -0.02, 1, 1)
#         )
#         fig.savefig(path_fig, dpi=800)

#
#  save_fig_scaling('legi_cluster8_320x640x640', '3d', 320, 640, 640)
#  save_fig_scaling('legi_cluster8_2160x2160', '2d', 2160, 2160)
#  save_fig_scaling('occigen_384x1152x1152', '3d', 384, 1152, 1152)
#  save_fig_scaling('beskow_384x1152x1152', '3d', 384, 1152, 1152)
#  save_fig_scaling('occigen_1152x1152x1152', '3d', 1152, 1152, 1152)
#  save_fig_scaling('beskow_1152x1152x1152', '3d', 1152, 1152, 1152)
