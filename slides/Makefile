main:=slides
frames:=latex/frames.pandoc.tex


$(main).pdf: latex/$(main).tex $(frames) latex/template_beamer.pandoc.tex
	cd latex && latexmk $(main).tex
	cp -f latex/$(main).pdf .

$(frames): $(sort $(wildcard sec*.md))
	pandoc \
		--slide-level 2 \
		-V classoption='notes' \
		-t beamer \
		$^ -o $@

clean:
	cd latex && latexmk -c $(main).tex
	rm -f $(frames)

