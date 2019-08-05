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



def get_options_from_yaml(path):
    """Read a options YAML file."""
    import ruamel.yaml as yaml

    yml = yaml.YAML()
    with open(path) as f:
        options = yml.load(f.read())

    # post-process options
    post_options = []
    for label, description in sorted(options.items()):
        if label.startswith("text_"):
            label = name = label.lstrip('text_')
        else:
            name = f'${label}$'
            label = label.lstrip('\\').lstrip('mathbf')

        post_options.append((label, name, description))

    return post_options


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

    options = get_options_from_yaml(options_file)
    template = get_template(template_file)

    out_file = os.fspath(options_file.parent / options_file.stem) + ".tex"
    render_template(template, {"entries": options}, out_file)
