"""

pip install tabulate


"""


from tabulate import tabulate

table = [
    ["512$^2$",  0.51, 8.01, 0.92, 0.82],
    ["1024$^2$", 2.69, 43.0, 3.48, 3.96]
]

headers = ["", r"\fluidpack{sim}", 'Dedalus', 'SpectralDNS', 'NS3D']

print(tabulate(table, headers, tablefmt="latex_raw"))
