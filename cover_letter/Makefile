#------------------------------------------------------------------------------
# This is a makefile tailored to work with the LaTeX documents for the
# Licentiate and PhD thesis (MechThesis).
#------------------------------------------------------------------------------


# Variables:
#
main = cover

TEX = pdflatex
TEX_FLAGS =

BIB = bibtex
BIB_FLAGS =


# Dependencies:
#
SRCS = $(main).tex          \
       list.tex

AUXS = $(main).aux

BBLS =

# Rules:
#
default: all

all: $(main)
#
$(main): $(SRCS) $(AUXS) $(BBLS)
	@echo building $(main) with $(TEX)
	@$(TEX) $(TEX_FLAGS) -draftmode $(main) #> /dev/null
	@$(TEX) $(TEX_FLAGS) $(main) #> /dev/null

$(AUXS): $(SRCS)
	@echo building $(main) with $(TEX) [for $@]
	@$(TEX) $(TEX_FLAGS) -draftmode $(main) #> /dev/null

%.bbl: %.aux $(main).bib
	@echo building $@ with $(BIB)
	@$(BIB) $(BIB_FLAGS) $(basename $@) #> /dev/null
#
clean:
	@echo cleaning thesis
	@rm -f *.ps *.dvi *.aux *.toc *.log *.out *.bbl *.blg *~ *.syntex.gz

%.pdf: %.tex
	latexmk -pdf $<
	latexmk -c $<


return_labels.pdf: return.pdf
	@pdftk $< cat 25 output $@
	@rm -f return.pdf
