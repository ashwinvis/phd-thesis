from pathlib import Path
import os

import panflute as pf


def extract_image_from_pdf_page(xObject):
    """https://gist.github.com/gstorer/f6a9f1dfe41e8e64dcf58d07afa9ab2a"""
    xObject = xObject['/Resources']['/XObject'].getObject()

    for obj in xObject:
        o = xObject[obj]
        if o['/Subtype'] == '/Image':
            return o
        else:
            return extract_image_from_pdf_page(o)


def detect_height(elem):
    url = Path(elem.url)
    if not url.exists() and not url.is_absolute():
        # Try parent dir
        new_url = url.parent.parent / url
        if new_url.exists():
            url = new_url
        else:
            raise
            pf.debug(f"WARNING: {url} not found")
            return "100%"

    width = int(elem.attributes["width"].rstrip('%'))
    if url.suffix == ".pdf":
        from PyPDF2 import PdfFileReader
        with open(url, "rb") as fp:
            pdf = PdfFileReader(fp)
            w, h = pdf.getPage(0).mediaBox[-2:]
            # o = extract_image_from_pdf_page(pdf.getPage(0))
            # w, h = (o['/Width'], o['/Height'])
    else:
        import imageio
        w, h, colors = imageio.imread(url).shape

    height = f"{width*h/w}%"
    return height


def action(elem, doc):
    """Automatically determines height attribute for images."""
    if doc.format in ('latex', 'beamer') and isinstance(elem, pf.Image):
        # pf.debug(elem)
        if "width" in elem.attributes and "height" not in elem.attributes:
            elem.attributes["height"] = detect_height(elem)

        return elem


def main(doc=None):
    return pf.run_filter(action, doc=doc)


if __name__ == '__main__':
    main()
