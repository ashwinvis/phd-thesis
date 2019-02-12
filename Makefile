#------------------------------------------------------------------------------
# This is a makefile tailored to work with the latex documents for the
# Licentiate and PhD thesis (MechThesis).
#------------------------------------------------------------------------------


# Variables:
#
kappa = overview
main = thesis
TEMPLATE_DIR = ./templates/mechthesis/

TEX = latexmk
TEX_FLAGS = -quiet -use-make -pdf -pdflatex="pdflatex -shell-escape %O %S"

BIB = bibtex
BIB_FLAGS =


# Dependencies:
#
SRCS = $(TEMPLATE_DIR)/jfm.bst              \
       $(TEMPLATE_DIR)/MechThesis.cls       \
       packages.tex         \
       commands.tex         \
       frontmatter.tex      \
       acknowledgements.tex \
       $(kappa).tex         \
       $(main).tex          \
       $(main).bib          \
       $(subst /,/paper.tex,$(wildcard paper*/))

AUXS = $(kappa).aux \
       $(main).aux  \
       $(main).toc  \
       $(main).pls  \
       $(main).psm  \
       $(subst /,/paper.aux,$(wildcard paper*/))

BBLS = $(kappa).bbl \
       $(subst /,/paper.bbl,$(wildcard paper*/))

# Rules:
#
default: all

all: $(main).pdf
#
$(main).pdf: $(SRCS) $(BBLS)
	@echo building $(main) with $(TEX)
	# @$(TEX) $(TEX_FLAGS) -draftmode $(main) #> /dev/null
	# @sed -i -e 's/toPaper/Paper/g' thesis.out	
	@$(TEX) $(TEX_FLAGS) $(main) #> /dev/null

$(AUXS): $(SRCS)
	@echo building $(main) with $(TEX) [for $@]
	@$(TEX) $(TEX_FLAGS) -draftmode $(main) #> /dev/null

%.bbl: %.aux $(main).bib
	@echo building $< with $(BIB)
	@$(BIB) $(BIB_FLAGS) $< #> /dev/null
#
clean: clean_papers clean_thesis

clean_thesis:
	@echo cleaning thesis
	@rm -f *.ps *.dvi *.aux *.toc *.log *.out *.bbl *.blg *.pls *.psm *~ *.syntex.gz

clean_papers:
	@echo cleaning papers
	@rm -f paper*/*.aux paper*/*.bbl paper*/*.blg

vimtex:
	# gvim $(name).tex --servername GVIM &
	# xterm -class GVIM -e vim $(name).tex --servername GVIM &
	NVIM_LISTEN_ADDRESS=GVIM nvim-gtk $(name).tex &

doit: vimtex $(name).pdf
	zathura $(name).pdf &

