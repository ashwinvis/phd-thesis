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


def detect_height(url):
    if url.endswith(".pdf"):
        from PyPDF2 import PdfFileReader
        with open(url, "rb") as fp:
            pdf = PdfFileReader(fp)
            w, h = pdf.getPage(0).mediaBox[-2:]
            # o = extract_image_from_pdf_page(pdf.getPage(0))
            # w, h = (o['/Width'], o['/Height'])
    else:
        import imageio
        w, h, colors = imageio.imread(url).shape

    height = f"{100*h/w}%"
    return height


def action_auto_height(elem, doc):
    """Automatically determines height attribute for images."""
    if isinstance(elem, pf.Image):
        # pf.debug(elem)
        if "width" in elem.attributes and "height" not in elem.attributes:
            elem.attributes["height"] = detect_height(elem.url)

        return elem


def main(doc=None):
    return pf.run_filter(action_auto_height, doc=doc)


if __name__ == '__main__':
    main()
