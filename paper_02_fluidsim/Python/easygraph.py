import functools
import os
import graphviz as gv
import matplotlib.pyplot as plt


class Digraph(object):
    GraphClass = gv.Digraph

    def __init__(self, path_file=None, label=''):
        self.path_file = path_file
        if path_file is None:
            self.graph = self.GraphClass()
            self.render = self.graph.render
        else:
            filename, ext = os.path.splitext(path_file)
            ext = ext.split('.')[-1]
            self.graph = self.GraphClass(format=ext)
            self.render = functools.partial(self.graph.render, filename=filename)

        # Function aliases
        self.add_node = self.graph.node
        self.add_edge = self.graph.edge

        self.styles = {
            'graph': {
                'label': label,
                'fontsize': '14',
                'fontcolor': 'black',
                'bgcolor': 'white',
                'rankdir': 'BT',
                'overlap': 'prism',
                'pack': 'True',
            },
            'nodes': {
                'fontname': 'DejaVu Sans',
                'shape': 'rect',
                'fontcolor': 'white',
                'color': 'black',
                'style': 'rounded, filled',
                'fillcolor': 'white',
            },
            'edges': {
                'style': 'solid',
                'color': 'black',
                'arrowhead': 'open',
                'fontname': 'Courier',
                'fontsize': '12',
                'fontcolor': 'white',
            }
        }

    def __repr__(self):
        return self.graph.source

    def add_nodes(self, nodes):
        graph = self.graph
        for n in nodes:
            if isinstance(n, tuple):
                graph.node(n[0], **n[1])
            else:
                graph.node(n)

    def add_edges(self, edges):
        graph = self.graph
        for e in edges:
            if isinstance(e[0], tuple):
                graph.edge(*e[0], **e[1])
            else:
                graph.edge(*e)

    def add_graph(self, other):
        if isinstance(other, self.__class__):
            self.graph.subgraph(other.graph)
        elif isinstance(other, gv.Digraph):
            self.graph.subgraph(other)

    def apply_styles(self, styles=None):
        if styles is None:
            styles = self.styles

        graph = self.graph
        graph.graph_attr.update(
            ('graph' in styles and styles['graph']) or {}
        )
        graph.node_attr.update(
            ('nodes' in styles and styles['nodes']) or {}
        )
        graph.edge_attr.update(
            ('edges' in styles and styles['edges']) or {}
        )
        return graph

    def show(self):
        try:
            from imageio import imread
            img = imread(self.path_file)
        except ImportError:
            img = plt.imread(self.path_file)
        plt.imshow(img)
        plt.show()


class Graph(Digraph):
    GraphClass = gv.Graph
