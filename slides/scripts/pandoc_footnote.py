"""Pandoc filter for footnotes in beamer which function. Forces [frame] option,
parses citation and returns a RawInline latex element instead."""
import panflute as pf


def elem2cite(elem, doc):
    """Safely extract a Cite element and convert to RawInline"""
    if isinstance(elem, pf.Cite):
        citation = elem.content[0]
        tex = pf.RawInline(str2cite(pf.stringify(citation)), format="latex")
        #  pf.debug(tex)
        return tex


def str2cite(word):
    r"""@Author -> \citet{Author}"""
    if word.startswith("@"):
        return rf"\citet{{{word.lstrip('@')}}}"

    return word


def action(elem, doc):
    if doc.format in ("beamer", "native") and isinstance(elem, pf.Note):
        elem = elem.walk(elem2cite)
        txt = pf.stringify(elem, newlines=False)
        tex = rf"\footnote<.->[frame]{{\tiny {txt}}}"
        elem = pf.RawInline(tex, format="latex")
    return elem


def prepare(doc):
    pf.debug(f'Starting {__file__} ...')


def finalize(doc):
    pf.debug(f'Ending {__file__} ...')


def main(doc=None):
    return pf.run_filter(action, prepare, finalize, doc=doc)


if __name__ == "__main__":
    main()
