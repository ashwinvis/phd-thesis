main:=slides
frames:=latex/frames.pandoc.tex
# js:=s5
js:=revealjs
content:=$(sort $(wildcard sec*.md))

$(main).pdf: latex/$(main).tex $(frames) latex/template_beamer.pandoc.tex
	cd latex && latexmk $(main).tex
	cp -f latex/$(main).pdf .

$(main).html: $(content)
	pandoc \
		--slide-level 2 \
		--standalone \
		--self-contained \
		-t $(js) \
		$^ -o $@

$(frames): $(content)
	pandoc \
		--slide-level 2 \
		-V classoption='notes' \
		-t beamer \
		$^ -o $@

clean:
	cd latex && latexmk -c $(main).tex
	rm -f $(frames)

