#!/usr/bin/env python
import types
import shutil
from fluidsim.solvers.ns3d.solver import Simul
from easygraph import Digraph
from base import curdir


g = Digraph(curdir + "/../Pyfig/fig_simul_obj_graphviz.png")
g_sim = Digraph()  # all objects attached to sim.
g_out = Digraph()  # sim.output.
g_oper = Digraph()  # sim.output.
g_doc = Digraph()  # first line of __doc__
g_met = Digraph()  # methods


def filter_object_dict(obj):
    return dict(
        [
            (key, attr)
            for key, attr in obj.__dict__.items()
            if not isinstance(attr, (types.MethodType, str, bool))
        ]
    )


def match(method_name):
    exact_match = [
        "fft_as_arg",
        "ifft_as_arg",
        "tendencies_nonlin",
        "compute",
        "plot",
        "dealiasing",
        "random_arrayK",
        "animate",
        "start",
        "params",
    ]
    partially_match = ["load", "_from_", "fft", "plot"]

    if method_name in exact_match and not method_name.startswith("_"):
        return method_name

    elif any(
        (name in method_name for name in partially_match)
    ) and not method_name.startswith(
        "_"
    ):
        return method_name

    else:
        return None


def filter_method_dict(obj):
    return dict(
        [
            (key, getattr(obj, key))
            for key in dir(obj)
            if isinstance(
                getattr(obj, key),
                (types.FunctionType, types.MethodType, types.BuiltinMethodType),
            )
            and match(key) is not None
        ]
    )


params = Simul.create_default_params()
with Simul(params) as sim:
    sim_dict = filter_object_dict(sim)
    output_dict = filter_object_dict(sim.output)
    oper_dict = filter_object_dict(sim.oper)
    sim_methods = {}
    output_methods = {}
    for key, attr in sim_dict.items():
        sim_methods[key] = filter_method_dict(attr)

    for key, attr in output_dict.items():
        output_methods[key] = filter_method_dict(attr)

    # Avoid duplicates
    del output_methods["oper"]
# print(sim.info)

shutil.rmtree(sim.output.path_run)

g.add_node("sim")

g.styles["graph"]["layout"] = "circo"
g.styles["graph"]["overlap"] = "prism"
g.styles["graph"]["overlap_scaling"] = "3.5"

g.styles["nodes"]["fontname"] = "monospace"
g.styles["nodes"]["fillcolor"] = "steelblue"
g.styles["nodes"]["shape"] = "hexagon"
g.styles["nodes"]["style"] = "filled"
g.apply_styles()


def add_nodes_edges(obj_dict, graph_node, obj_name):
    graph_node.add_nodes(obj_dict.keys())
    graph_node.styles["nodes"]["fillcolor"] = "black"
    graph_node.apply_styles()
    graph_node.add_edges([(obj_name, key) for key in obj_dict])


add_nodes_edges(sim_dict, g_sim, "sim")
add_nodes_edges(output_dict, g_out, "output")
add_nodes_edges(oper_dict, g_oper, "oper")

g_doc.add_nodes(
    [
        ("doc" + key, {"label": str(attr.__doc__).splitlines()[0]})
        for key, attr in sim_dict.items()
    ]
)
g_doc.styles["nodes"]["fillcolor"] = "gray"
g_doc.styles["nodes"]["fontcolor"] = "black"
g_doc.styles["edges"]["style"] = "dashed"
g_doc.apply_styles()
g_doc.add_edges([(key, "doc" + key) for key in sim_dict])

for node, node_methods in sim_methods.items():
    g_met.add_nodes([(node + key, {"label": key}) for key in node_methods])
    g_met.add_edges([(node, node + key) for key in node_methods])

for node, node_methods in output_methods.items():
    g_met.add_nodes([(key + node, {"label": key}) for key in node_methods])
    g_met.add_edges([(node, key + node) for key in node_methods])

g_met.styles["nodes"]["fontcolor"] = "black"
g_met.styles["nodes"]["shape"] = "rect"
g_met.styles["nodes"]["style"] = "bold"
g_met.styles["nodes"]["fillcolor"] = "beige"
g_met.styles["nodes"]["style"] = "rounded,filled"
# g_met.styles['nodes']['style'] = 'radial'
g_met.styles["edges"]["style"] = "dashed"
g_met.apply_styles()

g.add_graph(g_sim)
g.add_graph(g_out)
g.add_graph(g_met)
# g.add_graph(g_oper)
# g.add_graph(g_doc)

print(g)
g.render()
g.show()
