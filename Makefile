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
TEX_FLAGS = -quiet -draftmode
PDFLATEX_FLAGS = -quiet -use-make -pdf -pdflatex="pdflatex -shell-escape"

BIB = bibtex
BIB_FLAGS =


# Dependencies:
#
TEMPLATE_PAPER = templates/template_mechthesis_paper.tex
META_PAPER = $(wildcard paper*/paper.yml)
SRCS_PAPER = $(subst /,/paper.tex,$(wildcard paper*/))
SRCS = packages.tex         \
       commands.tex         \
       frontmatter.tex      \
       acknowledgements.tex \
       $(kappa).tex         \
       $(main).tex          \
       $(SRCS_PAPER)

# Template and BibTeX dependencies
#
DEPS = $(TEMPLATE_DIR)/MechThesis.cls       \
       $(TEMPLATE_DIR)/jfm.bst              \
       $(main).bib

AUXS = $(kappa).aux \
       $(main).aux  \
       $(main).toc  \
       $(main).pls  \
       $(main).psm  \
       $(subst /,/paper.aux,$(wildcard paper*/))

BBLS = $(kappa).bbl \
	   $(main).bbl \
       $(subst /,/paper.bbl,$(wildcard paper*/))

# Rules:
#
default: all

all: $(main).pdf
#
$(main).pdf: $(SRCS) $(DEPS) # $(BBLS)
	@echo building $(main) with $(TEX)
	# @$(TEX) $(TEX_FLAGS) -draftmode $(main) #> /dev/null
	# @sed -i -e 's/toPaper/Paper/g' thesis.out	
	@$(TEX) $(PDFLATEX_FLAGS) $(main) #> /dev/null

$(AUXS): $(SRCS) $(DEPS)
	@echo building $(main) with $(TEX) [for $@]
	@$(TEX) $(TEX_FLAGS) -draftmode $(main) #> /dev/null

%.bbl: %.aux $(main).bib
	@echo building $@  with $(BIB)
	@$(BIB) $(BIB_FLAGS) $< #> /dev/null
	# @$(BIB) $(BIB_FLAGS) $(basename $@) #> /dev/null

$(SRCS_PAPER): $(META_PAPER) $(TEMPLATE_PAPER)
	@echo building $@ with python
	@python templates/utils_render.py $< $(TEMPLATE_PAPER)
#
clean: clean_papers clean_thesis

cleanall: clean
	@rm -f  *.{ps,dvi,pdf}
	@rm -f  paper*/*.{ps,dvi,pdf}
	@rm -rf paper*/_minted-*

clean_thesis:
	@echo cleaning thesis
	@rm -f *.{aux,toc,log,out,bbl,blg,pls,psm,synctex.gz,fls,fdb_latexmk}

clean_papers:
	@echo cleaning papers
	@rm -f paper*/*.{aux,bbl,blg,fls,fdb_latexmk,log,out,pdf,synctex.gz}

vimtex:
	# gvim $(name).tex --servername GVIM &
	# xterm -class GVIM -e vim $(name).tex --servername GVIM &
	NVIM_LISTEN_ADDRESS=GVIM nvim-gtk $(name).tex &

doit: vimtex $(name).pdf
	zathura $(name).pdf &

