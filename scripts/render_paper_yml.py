#!/usr/bin/env python
"""Render a latex jinja template

Usage:
    render_paper_yml.py <options_file> <template_file>

Notes:
    See https://github.com/AKuederle/Py-Tex-automation-example

"""
import os
import re
import sys
from pathlib import Path

import jinja2


def get_options_from_file(path):
    """Read a options file.

    The pattern in the file is '%<key>:<value>'
    """
    with open(path) as f:
        content = f.read()
        keys = re.findall(r"%(.+):", content)
        values = re.findall(r":\s*([\w\W]+?)\s*(?:%|$)", content)

    options = dict(zip(keys, values))
    return options


def name_in_initials(name):
    """John Doe -> J. Doe"""
    name = name.split()
    first_name = name[:-1]
    last_name = name[-1]
    name = [n[0] + "." for n in first_name]
    name.append(last_name)
    return " ".join(name)


def get_options_from_yaml(path):
    """Read a options YAML file."""
    import ruamel.yaml as yaml

    yml = yaml.YAML()
    with open(path) as f:
        options = yml.load(f.read())

    if "dir" not in options or options["dir"] is None:
        options["dir"] = path.parent

    if len(options["authors"]) < 4:
        options["authors_short"] = [
            name_in_initials(name) for name in options["authors"][:-1]
        ]
        options["authors_short"].extend(
            [r"\&", name_in_initials(options["authors"][-1])]
        )
    else:
        options["authors_short"] = [
            name_in_initials(options["authors"][0]),
            "et al.",
        ]

    uniq_affiliations = list(set(options["affiliations"]))  # unique
    options["authors_aff"] = []
    for author, affiliation in zip(options["authors"], options["affiliations"]):
        options["authors_aff"].append(
            f"{author}$^{uniq_affiliations.index(affiliation) + 1}$"
        )
    options["enum_affiliations"] = [
        f"$^{i+1}$ {aff}" for i, aff in enumerate(uniq_affiliations)
    ]

    return options


def get_template(template_file):
    """Get a jinja template with latex tags.

    modified from http://eosrei.net/articles/2015/11/latex-templates-python-and-jinja2-generate-pdfs
    """
    latex_jinja_env = jinja2.Environment(
        block_start_string=r"%:",
        block_end_string=":%",
        variable_start_string=r"\VAR{",
        variable_end_string="}",
        comment_start_string=r"\#{",
        comment_end_string="}",
        line_statement_prefix="%%",
        line_comment_prefix="%#",
        trim_blocks=True,
        autoescape=False,
        loader=jinja2.FileSystemLoader(os.path.abspath("/")),
    )
    template = latex_jinja_env.get_template(os.path.realpath(template_file))
    return template


def render_template(template, insert_variables, out_path):
    """Render a template file"""

    rendered_template = template.render(**insert_variables)
    out_path = Path(out_path)
    build_d = Path(out_path).parent
    if not build_d.exists():  # create the build directory if not exisiting
        os.makedirs(build_d)

    with open(out_path, "w") as f:  # saves tex_code to output file
        f.write(rendered_template)

    print("Rendered", out_path)


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
    render_template(template, options, out_file)
