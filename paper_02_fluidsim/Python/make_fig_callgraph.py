#!/usr/bin/env python2
from __future__ import print_function
import os
from shutil import rmtree
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput as _GraphvizOutput, GephiOutput  # noqa

from pycallgraph import Config
from pycallgraph import GlobbingFilter

from fluiddyn.io.redirect_stdout import stdout_redirected
from fluidsim.base.solvers.pseudo_spect import SimulBasePseudoSpectral as Simul
# from fluidsim.solvers.ns2d.solver import Simul


VERTICAL = False
CIRCO = False


class GraphvizOutput(_GraphvizOutput):
    def prepare_graph_attributes(self):
        super(GraphvizOutput, self).prepare_graph_attributes()
        del self.graph_attributes['graph']['label']

        self.graph_attributes['graph']['pack'] = True
        if CIRCO:
            self.graph_attributes['graph']['layout'] = 'circo'
        self.graph_attributes['graph']['overlap'] = 'prism'

        self.graph_attributes['node']['style'] = 'rounded,filled'
        self.graph_attributes['node']['shape'] = 'rect,rotate=90'
        # self.graph_attributes['edge']['minlen'] = 1.0

    def generate_groups(self):
        output = super(GraphvizOutput, self).generate_groups()
        if VERTICAL:
            for i, item in enumerate(self.processor.groups()):
                groups, nodes = item
                output[i] = output[i][:-1] + 'edge [style=invis];'
                node_names = ['"{}"'.format(n.name) for n in nodes]
                output[i] += '->'.join(node_names) + '; }'

        return output

    def node_label(self, node):
        label = super(GraphvizOutput, self).node_label(node)
        label = label.split(r'\n')

        key = label[0].split('.')

        if 'fluidsim' in key:
            key.remove('fluidsim')

        if len(key) >= 3:
            module = '.'.join(key[:-2])
            cls = key[-2]
            if cls.islower():
                module = '.'.join((module, cls))
                cls = ''
            func = key[-1]
            label[0] = r'\n'.join((module, cls, func))

        # return r'\n'.join(label)
        return label[0]


def initialize_params():
    params = Simul.create_default_params()
    params.short_name_type_run = 'callgraph'
    params.nu_2 = 1.

    # params.FORCING = True
    # params.forcing.type = 'tcrandom'
    return params


def initialize_sim(params):
    with stdout_redirected():
        sim = Simul(params)
    return sim


if __name__ == '__main__':
    config = Config(max_depth=4)
    config.trace_filter = GlobbingFilter(exclude=[
        'pycallgraph.*',
        'numpy.*',
        'matplotlib.*',
        'fluiddyn.*',
        'contextlib.*',
        # 'main',
        '__main__.*'
    ])
    config.debug = True

    work_dir = os.path.abspath('../Pyfig/')
    if CIRCO:
        filename = work_dir + 'fig_callgraph_circo.svg'
    else:
        filename = work_dir + 'fig_callgraph.svg'

    filetype = filename.split('.')[1]
    output = GraphvizOutput(
        output_file=filename,
        output_type=filetype,
        font_name='Cousine',
        font_size=12,
        group_font_size=14
    )

    # output = GephiOutput(output_file='fig_callgraph.gdf')
    with PyCallGraph(output=output, config=config):
        params = initialize_params()
        sim = initialize_sim(params)

    with open(work_dir + 'fig_callgraph.dot', 'w') as dotfile:
        dotfile.write(output.generate())

    rmtree(sim.params.path_run)
