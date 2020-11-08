# Advancements in stratified flows through simulation, experiment and open research software development

| About                    |                                                                                               |
|--------------------------|-----------------------------------------------------------------------------------------------|
| Date and time of defence | Friday, 27 September 2019 kl 10:00                                                            |
| Location                 | F3, KTH, Lindstedtsvägen 26, Stockholm                                                        |
| Supervisor               | Erik Lindborg, Pierre Augier                                                                  |
| PDF                      | [urn:nbn:se:kth:diva-256564](http://urn.kb.se/resolve?urn=urn%3Anbn%3Ase%3Akth%3Adiva-256564) |
---

## Citation

```bibtex
@phdthesis{Mohanan-advancements-2019,
  author = {Mohanan, Ashwin Vishnu},
  title = {Advancements in Stratified Flows through Simulation, Experiment and Open Research Software Development},
  year = {2019}
}
```

## Requirements

* texlive
* biblatex
* latexmk
* python>=3.6
* git-lfs
* pandoc, pandoc-crossref (included in `pandoc-requirements.txt`)

I shall also list applications / CLI tools which prove to be handy for
several miscalleanous uses. Not mandatory, but good to have:

* zotero, better-bibtex (refrence management, deterministic BibTeX / BibLaTeX export)
* fzf, fzf-bibtex (fuzzy search to cite as you type, *note:* requires bibtool CLI tool)
* pandoc-citeproc (pandoc filter to process citations)
* zathura (vim-like pdf viewer)
* neovim / vim (needs no introduction)
* vim-pandoc-syntax (conceal and beautify markdown & LaTeX elements)
* ripgrep, sd (rust alternatives to grep and sed)
* inkscape (PDF, EPS editing)
* rubber (LaTeX error log parser)
* vale (natural language style checker)
* textidote (languagetool for LaTeX)
* texlive-localmanager (install missing packages from CTAN in ArchLinux)
* draw.io (create charts online / offline)
* ttf-humor-sans (for xkcd style plots)

## Getting started

Clone

    git clone --recursive https://github.com/ashwinvis/phd-thesis.git
    cd phd-thesis

Note: the `--recursive` option is important to clone the submodules. If you
forget to do that, execute:

    git submodule update --init --recursive

For texlive, I use:

    # pacman -S texlive-bibtexextra texlive-core texlive-latexextra texlive-science biber
    $ yay -S texlive-localmanager-git
    $ tllocalmgr install mnsymbol ccicons
    $ updmap -user --enable Map=ccicons.map
    # texhash

Use appropriate texlive packages suitable for your opertating system.

Setup a python virtual environment.

    make python

The requirements are pinned hard with versions specified. These are supposed to
work with Python 3.6.x and could be difficult to install with other versions.
In that case, use conda:

    conda env create --file environment.yml
    conda activate phd-thesis


## Workflows

**Always start by activating the virtual environment** `source pyenv/bin/activate`

Compile the whole thesis

    make -j

Compile a standalone PDF of a single chapter/section using pandoc

    make -j chapter_00_0_intro.pandoc.pdf

Compile a standalone PDF of all chapters in markdwon

    make -j chapters.pandoc.pdf

Watch for changes

    make watchthesis  # or watchchapter or watchchapters

Clean files

    make clean

Clean generated pdfs also

    make cleanall


## Troubleshooting

- ImageMagick might require extra privileges which are not enabled by default
  due to security concerns. However this is necessary for texlive package
  `epstopdf`. In `/etc/ImageMagick-7/policy.xml` add the following line:

  ```xml
  <policy domain="delegate" rights="none" pattern="gs" />
  ```

- You need to compile the thesis **before** compiling the slides. This is
  because the `Makefile` for the slides assumes the figures are all present.

- If you install a font and matplotlib does not recognize it, run:

  ```sh
  python -c 'from matplotlib import font_manager as fm; fm._rebuild()
  ```

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img
alt="Creative Commons License" style="border-width:0"
src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />
The **chapters** in this work
<span xmlns:cc="http://creativecommons.org/ns#"
property="cc:attributionName">Ashwin Vishnu Mohanan</span> are licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative
Commons Attribution 4.0 International License</a>.

Figures and contents of accompanying **papers** fall under various licenses,
which requires discretion. Feel free to [contact
me](https://ashwinvis.github.io/pages/contact.html) in case of any doubts.
