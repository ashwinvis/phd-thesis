import os
import shlex
import subprocess
from pathlib import Path

import PyPDF2 as pypdf
from PyPDF2 import PdfFileReader


def _setup_page_id_to_num(pdf, pages=None, _result=None, _num_pages=None):
    if _result is None:
        _result = {}
    if pages is None:
        _num_pages = []
        pages = pdf.trailer["/Root"].getObject()["/Pages"].getObject()
    t = pages["/Type"]
    if t == "/Pages":
        for page in pages["/Kids"]:
            _result[page.idnum] = len(_num_pages)
            _setup_page_id_to_num(pdf, page.getObject(), _result, _num_pages)
    elif t == "/Page":
        _num_pages.append(1)
    return _result


def outlines_pg_zoom_info(outlines, pg_id_num_map, result=None):
    if result is None:
        result = dict()
    if type(outlines) == list:
        for outline in outlines:
            outlines_pg_zoom_info(outline, pg_id_num_map, result)
    elif type(outlines) == pypdf.pdf.Destination:
        title = outlines["/Title"]
        result[title] = dict(
            title=outlines["/Title"],
            top=outlines["/Top"],
            left=outlines["/Left"],
            page=(pg_id_num_map[outlines.page.idnum] + 1),
        )
    return result


def get_page_numbers(pdf_name):
    with open(pdf_name, "rb") as f:
        pdf = PdfFileReader(f)
        total_pages = pdf.numPages
        # map page ids to page numbers
        pg_id_num_map = _setup_page_id_to_num(pdf)
        outlines = pdf.getOutlines()
        bookmarks_info = outlines_pg_zoom_info(outlines, pg_id_num_map)

    #  print(pg_id_num_map)
    #  print(bookmarks_info)
    pages = {meta["title"]: meta["page"] for meta in bookmarks_info.values()}

    return pages, total_pages


def pdf_separate(pdf_name, output_dir, version, dry_run=True):
    pages, total_pages = get_page_numbers(pdf_name)
    #  print("Pages:", pages)

    pages_range = {"Overview": ["1"]}
    for title, page in pages.items():
        if title.startswith("Paper") and "Abstracts" not in title:
            print(title)
            article_num = int(title[6])  # 7th character
            article_prev = list(pages_range.keys())[-1]
            pages_range[article_prev].append(str(page - 1))
            pages_range[f"Paper_{article_num}"] = [str(page)]

    article_prev = list(pages_range.keys())[-1]
    pages_range[article_prev].append(str(total_pages))
    print("Pages range:", pages_range)

    output_dir = Path.cwd() / output_dir / version
    if not dry_run:
        os.makedirs(output_dir, exist_ok=True)
    for part, prange in pages_range.items():
        prange = "-".join(prange)
        output = output_dir / ("_".join((version, part)) + ".pdf")
        cmd = f"pdftk {pdf_name} cat {prange} output {output}"
        print(cmd)
        if not dry_run:
            subprocess.run(shlex.split(cmd))


if __name__ == "__main__":
    pdf_separate("thesis.pdf", "print", "v3.0a", False)
