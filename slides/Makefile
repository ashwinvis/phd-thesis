FRAMES:=latex/frames.pandoc.tex


slides.pdf: latex/slides.tex $(FRAMES)
	cd latex && latexmk slides.tex
	cp -f latex/slides.pdf .

$(FRAMES): $(sort $(wildcard sec*.md))
	pandoc \
		--slide-level 2 \
		-V classoption='notes' \
		-t beamer \
		$^ -o $@

clean:
	cd latex && latexmk -c slides.tex
	rm -f $(FRAMES)

