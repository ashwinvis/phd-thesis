main:=slides
frames:=latex/frames.pandoc.tex
# js:=s5
js:=revealjs
content:=$(sort $(wildcard sec*.md))

pandoc_flags:= # --slide-level 2
latexmk_flags:= -silent -pvc -deps

$(main).pdf: latex/$(main).tex $(frames) latex/template_beamer.pandoc.tex
	cd latex && latexmk $(latexmk_flags) $(main).tex
	cp -f latex/$(main).pdf .

$(main).html: $(content)
	pandoc \
		$(pandoc_flags) \
		--standalone \
		--self-contained \
		-t $(js) \
		$^ -o $@

$(frames): $(content)
	pandoc \
		$(pandoc_flags) \
		-V classoption='notes' \
		-t beamer \
		$^ -o $@

clean:
	cd latex && latexmk -c $(main).tex
	rm -f $(frames)

