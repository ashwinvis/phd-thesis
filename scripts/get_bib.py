"""Receive file served by Zotero + Better BibTeX plugin."""
import time

import requests

FORMAT = "biblatex"
SRC = "thesis." + FORMAT
URL = "http://localhost:23119/better-bibtex/collection?/1/" + SRC
SAVE_AS = "thesis.bib"  # + FORMAT

print("Fetching", SRC, end="... ")
tstart = time.time()
try:
    response = requests.get(URL, timeout=2)
except requests.exceptions.Timeout:
    raise IOError(f"Cannot fetch {SRC}. Is Zotero open?")

with open(SAVE_AS, "w") as bib:
    bib.write(response.content.decode("utf8"))

tend = time.time()
print(f"Saved as {SAVE_AS} in {(tend - tstart):.3f} seconds")
