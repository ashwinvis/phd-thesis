import re

import panflute as pf


def create_citation(label, prefix=""):
    pandoc_label = f"[@{prefix}{label}]"
    elem = pf.Cite(pf.Str(pandoc_label))
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
        pf.debug(f"No label in {text}")


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
        if r"\label" in text:
            env = "align"
        else:
            env = "align*"
            # labels = extract_latex_labels(text)

        if r"\begin{aligned}" in text:
            return pf.RawInline(
                "\n" + text.replace("{aligned}", f"{{{env}}}") + "\n", format="tex"
            )

    if doc.format.startswith("markdown"):
        if isinstance(elem, pf.RawInline) and elem.format == "tex":
            label = pf.stringify(elem).lstrip(r"\eqref{").rstrip("}")
            return create_citation(label)
        elif isinstance(elem, pf.Link) and "reference-type" in elem.attributes:
            if elem.attributes["reference-type"] in ("eqref", "ref"):
                label = elem.url.lstrip("#")
                return create_citation(label)


def main(doc=None):
    return pf.run_filter(action, doc=doc)


if __name__ == "__main__":
    main()
