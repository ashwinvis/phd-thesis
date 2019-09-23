from pathlib import Path
import re

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
        new_url = Path("..") / url
        if new_url.exists():
            url = new_url
        else:
            raise FileNotFoundError(f"Neither {url} nor {new_url} found")

    r = re.compile(r'([0-9]*[.])?[0-9]+')
    w = elem.attributes["width"]
    width = float(r.match(w).group(0))
    unit = r.sub("", w)

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

    w, h = (float(i) for i in (w, h))
    if url.suffix == ".eps":
        height = f"{width*w/h}{unit}"  # TODO: wtf!
    else:
        height = f"{width*h/w}{unit}"

    return height


def action(elem, doc):
    """Automatically determines height attribute for images."""
    if doc.format in ('latex', 'beamer', 'native') and isinstance(elem, pf.Image):
        if "width" in elem.attributes and "height" not in elem.attributes:
            height = detect_height(elem)
            if height:
                elem.attributes["height"] = height

        return elem


def prepare(doc):
    pf.debug(f'Starting {__file__} ...')


def finalize(doc):
    pf.debug(f'Ending {__file__} ...')


def main(doc=None):
    return pf.run_filter(action, prepare, finalize, doc=doc)


if __name__ == '__main__':
    main()
