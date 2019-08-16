import subprocess
from itertools import chain
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import STOPWORDS, ImageColorGenerator, WordCloud

cwd = Path(__file__).absolute().parent
root = cwd.parent.parent


class args:
    width = 600 * 4
    height = 250 *4
    max_words = 500
    #  output = None
    #  output = "plot"
    output = cwd / 'wordcloud.png'
    mask = cwd / "mask_darkblue_rect.png"
    colormask = mask


body = ""
for filename in chain(
    root.glob("chapter*.md"),
    (root / "chapter_02_open_science.tex",),
    root.glob("paper*/**/article.tex")
):
    if filename.suffix == ".tex":
        plain_text = subprocess.check_output(("detex", "-n", filename), text=True)
        body += plain_text
    else:
        with open(filename) as f:
            body += f.read()


blacklist = {
    "code", "package", "language", "one", "use", "time", "tool",
    "kappa", "using", "used", "Matlab", "emph", "many", "footnote",
    "mathbf", "fnref", "eq", "https", "http", "href", "url", "hat", "theta",
    "will", "Thus", "found", "F_h", "u_c", "two", "end", "org", "cite",
    "item", "begin", "Bmatrix", "textbf", "label", "caption", "partial_t",
    "see", "delta", "figure", "equation", "sim", "run", "different", "value",
    "term", "itemize", "example", "may", "become", "three", "case", "eqnarray",
    "now", "even", "function",
    "citep", "shown", "pack", "several", "make", "codeinline", "src", "fig",
    "raw", "html", "latex", "bf", "img", "div", "math", "png", "alt", "align",
    "green", "Ding", "link", "nbsp", "cdot", "nabla", "frac", "partial", "eta",
    "style", "width", "right", "left", "center", "Result", "drawing",
}
stopwords = set(STOPWORDS).union(blacklist)


def imread(f):
    return (np.array(Image.open(f)))


mask = imread(args.mask)
color_func = ImageColorGenerator(imread(args.colormask))
wordcloud = WordCloud(
    background_color="white",
    stopwords=stopwords,
    width=args.width,
    height=args.height,
    max_words=args.max_words,
    margin=0,
    mask=mask,
    color_func=color_func,
)
wordcloud.generate(body)


if args.output:
    if args.output != "plot":
        dpi = 600
        plt.rc("figure", dpi=dpi)
        figsize = np.array([args.width, args.height]) / dpi
        fig, ax = plt.subplots(figsize=figsize)
        # fig, ax = plt.subplots()
    else:
        ax = plt

    ax.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout()

    if args.output == "plot":
        plt.show()
    else:
        print("Saving to", args.output)
        fig.savefig(args.output)
