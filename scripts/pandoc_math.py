import re

import panflute as pf


def create_citation(label, prefix=""):
    pandoc_label = f"[@{prefix}{label}]"
    elem = pf.RawInline(pandoc_label)
    #  pf.debug(elem)
    return elem


def extract_latex_labels(text):
    p = re.compile(
        r"""
        \\label{
            ([0-9a-zA-Z:_]+)  # capture within the label
        }
        """,
        re.VERBOSE,
    )
    labels = p.findall(text)
    if labels:
        return labels
    else:
        return []  # "No label in {text}"


def action(elem, doc):
    r"""Handles \begin{align} \label \eqref and \ref while converting from LaTeX.

    Why
    ---
    * Pandoc converts \begin{align} -> \begin{aligned} implicitly which does
    not handle multiple labels

    * Pandoc does not have a mechanism to handle \eqref or \ref, but
    pandoc-crossref has one, so we re-engineer an expression which suits
    the latter

    """
    if isinstance(elem, pf.Math) and elem.format == "DisplayMath":
        text = pf.stringify(elem)

        for label in extract_latex_labels(text):
            if not label.startswith("eq:"):
                text = text.replace(rf'\label{{{label}}}', rf'\label{{eq:{label}}}')

        if r"\begin{aligned}" in text:
            if r"\label" in text:
                env = "align"
            else:
                env = "align*"

            return pf.RawInline(
                "\n" + text.replace("{aligned}", f"{{{env}}}") + "\n", format="tex"
            )
        else:
            return pf.Math(text, format=elem.format)

    if doc.format.startswith("markdown"):
        label = ""
        if isinstance(elem, pf.RawInline) and elem.format == "tex":
            label = pf.stringify(elem).lstrip(r"\eqref{").rstrip("}")
            return create_citation(label, 'eq:')
        elif isinstance(elem, pf.Link) and "reference-type" in elem.attributes:
            label = elem.url.lstrip("#")
            if elem.attributes["reference-type"] == "eqref":
                return create_citation(label, "eq:")
            elif elem.attributes["reference-type"] == "ref":
                return create_citation(label)


def main(doc=None):
    return pf.run_filter(action, doc=doc)


if __name__ == "__main__":
    main()
