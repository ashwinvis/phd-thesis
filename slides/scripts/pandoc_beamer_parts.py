"""pandoc-beamer-parts is a panflute pandoc filter to add parts to latex beamer
presentations."""

import panflute as pf


def action(elem, doc):
    if isinstance(elem, pf.elements.RawInline):  # and doc.format == "beamer":
        if elem.text.startswith('\\part{') and elem.text.endswith('}'):
            body = pf.convert_text(elem.text[6:-1], output_format='latex')
            para = pf.convert_text('\\part oso{{{}}}'.format(body))[0]
            return para#pf.RawInline(para.content[0])
    return elem


def main(doc=None):
    return pf.run_filter(action, doc=doc)


if __name__ == '__main__':
    main()
