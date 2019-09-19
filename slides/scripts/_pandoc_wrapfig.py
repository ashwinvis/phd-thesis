#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pandoc filter to allow variable wrapping of LaTeX/pdf documents
through the wrapfig package.

Simply add a " {?}" tag to the end of the caption for the figure, where
? is an integer specifying the width of the wrap in inches. 0 will
cause the width of the figure to be used.

"""
import panflute as pf
# FIXME: Not working yet


def wrapfig(elem, doc):
    attrs = elem.attributes
    caption = ''.join(pf.stringify(e) for e in elem.content)
    #  caption = elem.content
    #  pf.debug(caption)
    target = elem.url
    fmt = "latex"

    # Strip tag
    size = attrs.get("width")
    if "lineheight" in attrs:
        lineheight = attrs.lineheight
        latex_begin = r"\begin{wrapfigure}[" + lineheight + "]{l}{" + size + "}"
    else:
        latex_begin = r"\begin{wrapfigure}{l}{" + size + "}"

    if len(caption) > 0:
        latex_fig = r"\centering\includegraphics{" + target + "}\caption{"
        latex_end = r"}\end{wrapfigure}"
        return pf.RawInline(latex_begin + latex_fig + caption + latex_end, fmt)
        # return list(pf.RawInline(latex_begin + latex_fig), caption, pf.RawInline(latex_end))
    else:
        latex_fig = r"\centering\includegraphics{" + target[0] + "}"
        latex_end = r"\end{wrapfigure}"
        return pf.RawInline(latex_begin + latex_fig + latex_end, fmt)


def action(elem, doc):
    """Use wrapfig instead of includegraphics."""
    if (
        doc.format in (
            "latex", "beamer",
            "native", "json",
        ) and isinstance(
            elem, pf.Image
        )
    ):
        if "wrap" in elem.attributes:
            return wrapfig(elem, doc)
        else:
            return elem


def main(doc=None):
    return pf.run_filter(action, doc=doc)


if __name__ == "__main__":
    main()
