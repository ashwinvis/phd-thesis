import matplotlib.pyplot as plt
import networkx as nx
from networkx.readwrite.adjlist import read_adjlist

colors = {
    "royalblue": (
        "Python",
        "Cython",
        "Pythran",
        "numpy.f2py",
        "mpi4py",
        "transonic",
        "h5py",
        "h5netcdf",
        "NumPy",
        "SciPy",
        "IPython",
        "Jupyter",
        "SymPy",
        "xarray",
        "pandas",
        "matplotlib",
        "fluiddyn",
        "fluidsim",
        "fluidfft",
    ),
    "pink": (
        "C",
        "C++",
        "xproject",
        "xsimd",
        "HDF5",
        "FFTW",
        "PFFT",
    ),
    "purple": ("Fortran", "P3DFFT"),
    "slategrey": ("CUDA", "cuFFT", "OpenMP", "MPI", "SIMD"),
}

G = read_adjlist("graph.txt")
node_color = []
for node in G.nodes():
    color = [k for k, v in colors.items() if node in v]
    if color:
        # node_color.append(color[0])
        G.node[node]["value"] = color[0]
    else:
        raise ValueError("No color assigned for %s" % node)

#  nx.draw(G, with_labels=True, node_shape="s", node_color=node_color,
#          node_size=1000,)
from nxviz.plots import CircosPlot
c = CircosPlot(
    G,
    node_color="value",
    node_order="value",
    node_labels=True,
    # , node_color=node_color
    fontfamily="monospace",
)
c.draw()
plt.tight_layout()
plt.savefig("../dependency.pdf")
plt.show()
