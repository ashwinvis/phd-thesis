# Files
main:=slides
content:=frames.pandoc.md

# Options
# js:=s5
js:=revealjs
content_tex:=$(subst .md,.tex,$(content))
pandoc_filters:= $(subst ./,-F ./,$(wildcard ./scripts/pandoc_*.py))

# Flags
pandoc_flags:= --slide-level 2 $(pandoc_filters)
latexmk_flags:= -silent # -deps


watch: $(main).pdf
	pgrep -af evince && evince $(main).pdf &
	cd latex && latexmk -pvc $(latexmk_flags) $(main).tex

pres: $(main).pdf
	pgrep -af pympress || pympress -t 30 $< &

$(main).pdf: latex/$(main).tex $(content_tex) latex/template_beamer.pandoc.tex
	cd latex && latexmk $(latexmk_flags) $(main).tex

%.pandoc.html: %.pandoc.md
	pandoc \
		$(pandoc_flags) \
		--standalone \
		--self-contained \
		-t $(js) \
		$^ -o $@

%.pandoc.tex: %.pandoc.md
	pandoc \
		$(pandoc_flags) \
		-t beamer \
		$^ -o $@

clean:
	cd latex && latexmk -c $(main).tex
	rm -f $(content_tex)
