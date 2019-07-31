name := milestone1st

LATEX := pdflatex -shell-escape -synctex=1

define watchdog =
	@echo -e "execute watchdog: on pattern $(1): run $(2)"
	nohup watchmedo shell-command --patterns=$(1) --command=$(2) --drop
	# 2>watch.log&
endef


.PHONY: all clean cleanall

all: $(name).pdf

figures:
	python py/make_figs.py save_for_tex
	python py/make_table.py

$(name).pdf: $(name).tex figures sec_open_science.latex
	latexmk -pdf -pdflatex="$(LATEX)" $(name).tex

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

%.latex: %.md
	@pandoc \
		-F ./py/pandoc_auto_height.py \
		-F pandoc-crossref \
		-r markdown-auto_identifiers \
		--natbib \
		$< -o $@

clean:
	rm -f *.log *.aux *.out *.bbl *.blg *.tmp *.fdb_latexmk *.fls *.synctex.gz
	rm -rf _minted-$(name)

cleanpdf: clean
	rm -f $(name).pdf

cleanall: cleanpdf
	rm -rf tmp

watch:
	$(call cprint,"watching for changes")
	$(call watchdog,"*.{md,tex}",'make $(name).pdf')
