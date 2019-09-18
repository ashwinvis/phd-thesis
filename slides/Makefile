# Files
main:=slides
content:=frames.pandoc.md
pandoc_filters:=$(wildcard ./scripts/pandoc_*.py)

deps:=latex/$(main).tex $(content_tex) latex/template_beamer.pandoc.tex

# Options
# js:=s5
js:=revealjs
content_tex:=$(subst .md,.tex,$(content))

# Flags
pandoc_flags:= --slide-level 3 $(subst ./,-F ./,$(pandoc_filters))
latexmk_flags:= -silent

# Env variables
# TEXINPUTS := ~/src/latex/phd-thesis/slides/:
# export TEXINPUTS

watch: $(main).pdf
	pgrep -af evince && evince $(main).pdf &
	cd latex && latexmk -pvc $(latexmk_flags) $(main).tex

pres: $(main).pdf
	pgrep -af pympress || pympress -t 30 $< &

$(main).pdf: $(deps)
	cd latex && latexmk -silent $(main).tex

latex/$(main).aux: $(deps)
	cd latex && latexmk -pdflatex='pdflatex -draftmode -interaction=nonstopmode' $(main).tex

%.bbl: %.bcf %.aux $(BIB_FILE)
	cd latex && biber $(main)

log: $(deps)
	cd latex && rubber-info $(main)

%.pandoc.html: %.pandoc.md $(pandoc_filters)
	pandoc \
		$(pandoc_flags) \
		--standalone \
		--self-contained \
		--natbib \
		-t $(js) \
		$< -o $@

%.pandoc.tex: %.pandoc.md $(pandoc_filters)
	pandoc \
		$(pandoc_flags) \
		-t beamer \
		--natbib \
		$< -o $@

clean:
	cd latex && latexmk -c $(main).tex
	rm -f $(content_tex)

cleanall: clean
	cd latex && latexmk -C $(main).tex
