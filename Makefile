#------------------------------------------------------------------------------
# This is a makefile tailored to work with the latex documents for the
# Licentiate and PhD thesis (MechThesis).
#------------------------------------------------------------------------------


# Variables:
#
kappa := overview
main := thesis
# paper := paper?
paper := paper_0*
TEMPLATE_DIR := ./templates/mechthesis/

TEX := pdflatex
DRAFT_FLAGS := -draftmode -interaction=nonstopmode -shell-escape
FINAL_FLAGS := -interaction=nonstopmode -shell-escape

BIB := biber
BIB_FLAGS :=
BIB_FILE := $(main).bib

red:="\033[0;31m"
end:="\033[0m"

REDIRECT := | tail -n 5
# REDIRECT := 1> /dev/null
# REDIRECT := # no redirect

# Dependencies:
#
TEMPLATE_PAPER = templates/template_mechthesis_paper.tex
META_PAPER = $(wildcard $(paper)/paper.yml)
SRCS_PAPER = $(subst /,/paper.tex,$(wildcard $(paper)/))
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
       $(BIB_FILE)

AUXS = $(kappa).aux \
       $(main).aux \
       $(subst /,/paper.aux,$(wildcard $(paper)/))
       # $(main).toc  \

BBLS = $(main).bbl \
       $(main).bcf

MKDWN2TEX = $(subst .md,.latex,$(wildcard chapter*.md))

# Rules:
#
.PHONY: default all clean clean_papers clean_thesis clean_minted cleanall vimtex doit
.NOPARALLEL: $(main).pdf log

default: all

all: log
#
$(main).pdf: $(SRCS) $(DEPS) $(AUXS) $(BBLS)
	@echo building $(main) with $(TEX)
	# @$(TEX) $(DRAFT_FLAGS) $(main) $(REDIRECT)
	@sed -i -e 's/toPaper/Paper/g' thesis.out	
	@$(TEX) $(FINAL_FLAGS) $(main) $(REDIRECT)

$(AUXS): $(SRCS) $(DEPS) $(MKDWN2TEX)
	@echo building $(main) with $(TEX) for $@
	@$(TEX) $(DRAFT_FLAGS) $(main) $(REDIRECT)

%.bcf: %.aux
	@echo $(red)building $@ with $< $(end)

%.bbl: %.aux $(BIB_FILE)
	@echo building $@ with $(BIB)
	@$(BIB) $(BIB_FLAGS) $(main) #> /dev/null
	# @$(BIB) $(BIB_FLAGS) $(basename $@) #> /dev/null

%.tex: %.yml $(TEMPLATE_PAPER)
	@echo building $@ with python
	@python templates/utils_render.py $< $(TEMPLATE_PAPER)

chapter_%.latex: chapter_%.md
	@echo building $@ with pandoc
	@pandoc --natbib $< -o $@

chapter_%.pandoc.tex: chapter_%.md templates/mkdwn-header.tex
	@echo building $@ with pandoc
	@pandoc --biblatex \
		--bibliography $(BIB_FILE) \
		-s --filter pandoc-citeproc \
		--filter pandoc-crossref \
		--top-level-division=chapter \
		--include-in-header templates/mkdwn-header.tex \
		--from markdown+yaml_metadata_block+table_captions \
		$< -o $@

chapter_%.pandoc.pdf: chapter_%.pandoc.tex
	@echo building $@ with latexmk
	@latexmk -silent -use-make -pdf $<

$(BIB_FILE):
	@python scripts/get_bib.py

log: $(main).pdf
	rubber-info $(main)

colorlog: $(main).log
	rubber-info $(main) | ccze -m ansi

clean: clean_papers clean_thesis

cleanall: clean
	@echo cleaning generated ps,dvi,pdf,paper.tex
	@rm -f  *.{ps,dvi,pdf}
	@rm -f paper*/paper.tex

clean_minted:
	@rm -rf _minted-$(main) $(paper)/_minted-*

clean_thesis:
	@echo cleaning thesis
	@rm -f *.{aux,toc,log,out,bbl,bcf,blg,pls,psm,synctex.gz,fls,fdb_latexmk}

clean_papers:
	@echo cleaning papers
	@rm -f paper*/*.{aux,bbl,blg,fls,fdb_latexmk,log,out,synctex.gz}

todo:
	@# grep -r --color=tty '%.*[Tt][Oo][Dd][Oo]:'
	@ack '%.*[Tt][Oo][Dd][Oo]:'

vimtex:
	# gvim $(name).tex --servername GVIM &
	# xterm -class GVIM -e vim $(name).tex --servername GVIM &
	# NVIM_LISTEN_ADDRESS=GVIM 
	nvim-qt $(main).tex 2> /dev/null &

doit: vimtex $(main).pdf
	zathura $(main).pdf &
