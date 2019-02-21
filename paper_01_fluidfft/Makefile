
name := fluidfft_paper

LATEX := pdflatex -shell-escape -synctex=1

.PHONY: all clean

all: $(name).pdf

revision.tex:
	hg cat -r 0.2.0 $(name).tex > $(name)_submitted.tex
	latexdiff -c PICTUREENV=minted $(name)_submitted.tex $(name).tex > revision.tex
	rm -f $(name)_submitted.tex

revision.pdf: revision.tex
	latexmk -pdf -pdflatex="$(LATEX)" revision.tex
	rm -f revision.tex

revision: revision.tex revision.pdf clean

rebuttal.pdf: rebuttal.md
	pandoc $< -o $@

clean:
	rm -f *.log *.aux *.out *.bbl *.blg *.tmp
	rm -rf _minted-*

cleanall: clean
	rm -f $(name).pdf
	rm -rf tmp

edittex:
	emacs $(name).tex &

startworking: edittex $(name).pdf
	evince $(name).pdf &

vimtex:
	# gvim $(name).tex --servername GVIM &
	# xterm -class GVIM -e vim $(name).tex --servername GVIM &
	NVIM_LISTEN_ADDRESS=GVIM nvim-qt $(name).tex &

doit: vimtex $(name).pdf
	zathura $(name).pdf &

figures:  tmp/fig_microbench.pdf
	cd python && python makefile_figures.py

$(name).pdf: figures $(name).log
	@# $(LATEX) $(name).tex
	@if [ `grep "Package rerunfilecheck Warning: File" $(name).log | wc -l` != 0 ]; then $(LATEX) $(name).tex; fi
	@if [ `grep "Rerun to get cross-references right." $(name).log | wc -l` != 0 ]; then $(LATEX) $(name).tex; fi
	@if [ `grep "Package natbib Warning: Citation(s) may have changed." $(name).log | wc -l` != 0 ]; then $(LATEX) $(name).tex; fi

$(name).log: $(name).tex $(name).bbl
	$(LATEX) $(name).tex

$(name).bbl: $(name).aux ../bib.bib
	bibtex $(name).aux

$(name).aux: $(name).tex
	$(LATEX) $(name).tex

tmp/fig_microbench.pdf: microbench/make_fig_bar.py
	python microbench/make_fig_bar.py save
