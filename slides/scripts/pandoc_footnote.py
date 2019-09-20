"""Pandoc filter for footnotes in beamer which function. Forces [frame] option,
parses citation and returns a RawInline latex element instead."""
import panflute as pf


def cite(word):
    """@Author -> \citet{Author}"""
    if word.startswith("@"):
        return rf"\citet{{{word.lstrip('@')}}}"
    else:
        return word


def natbib_citations(txt):
    return " ".join(cite(word) for word in txt.split(" "))


def action(elem, doc):
    if doc.format in ("beamer", "native") and isinstance(elem, pf.Note):
        txt = pf.stringify(elem, newlines=False)
        txt = natbib_citations(txt)
        tex = rf"\footnote<.->[frame]{{{txt}}}"
        elem = pf.RawInline(tex, format="latex")
    return elem


def main(doc=None):
    return pf.run_filter(action, doc=doc)


if __name__ == "__main__":
    main()
