#!/usr/bin/env python
"""Render a latex jinja template

Usage:
    render_glossary_yml.py <options_file> <template_file>

Notes:
    See https://github.com/AKuederle/Py-Tex-automation-example

"""
import os
import sys
from pathlib import Path

from render_paper_yml import get_template, render_template


GREEK = [
    "Alpha",
    "Beta",
    "Gamma",
    "Delta",
    "Epsilon",
    "Zeta",
    "Eta",
    "Theta",
    "Iota",
    "Kappa",
    "Lamda",
    "Mu",
    "Nu",
    "Xi",
    "Omicron",
    "Pi",
    "Rho",
    "Sigma",
    "Tau",
    "Upsilon",
    "Phi",
    "Chi",
    "Psi",
    "Omega",
    "alpha",
    "beta",
    "gamma",
    "delta",
    "epsilon",
    "zeta",
    "eta",
    "theta",
    "iota",
    "kappa",
    "lamda",
    "mu",
    "nu",
    "xi",
    "omicron",
    "pi",
    "rho",
    "sigma",
    "tau",
    "upsilon",
    "phi",
    "chi",
    "psi",
    "omega",
]


def get_options_from_yaml(path):
    """Read a options YAML file."""
    import ruamel.yaml as yaml

    yml = yaml.YAML()
    with open(path) as f:
        options = yml.load(f.read())

    # post-process options
    glossary = []
    acronym = []
    for label, description in options.items():
        if label.startswith("acr_"):
            label = name = label.replace("acr_", "")
            acronym.append((label, name, description))
        else:
            name = f"${label}$"
            for char in r"\{^},":
                label = label.replace(char, "")
            for word in ("mathbf", "mathcal", "hat"):
                if word in label:
                    label = label.replace(word, "") + "_" + word
            if any(label.startswith(greek_alphabet) for greek_alphabet in
                   GREEK):
                label = "aa_" + label

            glossary.append((label, name, description))

    return sorted(glossary), sorted(acronym)


if __name__ == "__main__":
    try:
        from docopt import docopt

        argv = docopt(__doc__)
        options_file = Path(argv["<options_file>"])
        template_file = Path(argv["<template_file>"])
    except ImportError:
        argv = sys.argv
        options_file = Path(argv[1])
        template_file = Path(argv[2])

    glossary, acronym = get_options_from_yaml(options_file)
    template = get_template(template_file)

    out_file = os.fspath(options_file.parent / options_file.stem) + ".tex"
    render_template(
        template, {"glossary": glossary, "acronym": acronym}, out_file
    )
