#------------------------------------------------------------------------------
# This is a makefile tailored to work with the latex documents for the
# Licentiate and PhD thesis (MechThesis).
#------------------------------------------------------------------------------


# Variables:
#
kappa := overview
main := thesis
chapter := chapter_00_open_science
paper := paper_0*
TEMPLATE_DIR := ./templates/mechthesis/

TEX := pdflatex
DRAFT_FLAGS := -draftmode -interaction=nonstopmode -shell-escape
FINAL_FLAGS := -interaction=nonstopmode -shell-escape

VIM := nvim-gtk
VIM_FLAGS := -- +'set backupcopy=yes'

BIB := biber
BIB_FLAGS :=
BIB_FILE := $(main).bib

red:="\033[0;31m"
end:="\033[0m"

define cprint =
	@echo -e $(red)$(1)$(end)
endef

REDIRECT := | tail -n 5
# REDIRECT := 1> /dev/null
# REDIRECT := # no redirect

RUBBER_INFO := $(shell command -v rubber-info 2> /dev/null)

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
       $(subst /,/paper.aux,$(wildcard $(paper)/))
       # $(main).aux \
       # $(main).toc  \

BBLS = $(main).bbl \
       $(main).bcf

MKDWN2TEX = $(subst .md,.latex,$(wildcard chapter*.md))

# Rules:
#
.PHONY: default all clean clean_papers clean_thesis clean_minted cleanall vimtex doit
.NOPARALLEL: $(main).pdf log watch

default: all

all: $(main).pdf log
#
$(main).pdf: $(SRCS) $(DEPS) $(AUXS) $(BBLS)
	$(call cprint,"building $@ with $(TEX)")
	# @$(TEX) $(DRAFT_FLAGS) $(main) $(REDIRECT)
	@sed -i -e 's/toPaper/Paper/g' thesis.out	
	@$(TEX) $(FINAL_FLAGS) $(main) $(REDIRECT)

$(AUXS): $(main).aux

$(main).aux: $(SRCS) $(DEPS) $(MKDWN2TEX)
	$(call cprint,"building $@ with $(TEX)")
	@$(TEX) $(DRAFT_FLAGS) $(main) $(REDIRECT)

%.bcf: %.aux
	$(call cprint,"building $@ with $<")

%.bbl: %.aux $(BIB_FILE)
	$(call cprint,"building $@ with $(BIB)")
	@$(BIB) $(BIB_FLAGS) $(main) #> /dev/null
	# @$(BIB) $(BIB_FLAGS) $(basename $@) #> /dev/null

%.tex: %.yml $(TEMPLATE_PAPER)
	$(call cprint,"building $@ with python templates/utils_render.py")
	@python templates/utils_render.py $< $(TEMPLATE_PAPER)

chapter_%.latex: chapter_%.md
	$(call cprint,"building $@ with pandoc")
	@pandoc \
		--natbib \
		-F pandoc-crossref \
		$< -o $@

chapter_%.pandoc.tex: chapter_%.md templates/mkdwn-header.tex
	$(call cprint,"building $@ with pandoc")
	@pandoc \
		-F pandoc-crossref \
		-F pandoc-citeproc \
		--bibliography $(BIB_FILE) \
		--csl templates/journal-of-fluid-mechanics.csl \
		--standalone \
		--top-level-division=chapter \
		--from markdown+table_captions \
		--metadata-file=pandoc-meta.yml \
		$< -o $@
		# --biblatex \

chapter_%.pandoc.pdf: chapter_%.pandoc.tex
	$(call cprint,"building $@ with latexmk")
	@latexmk -silent -use-make -pdf $<

$(BIB_FILE):
	$(call cprint,"building $@ with python scripts/get_bib.py")
	@python scripts/get_bib.py

log:
	$(call cprint,"printing $@")
ifndef RUBBER_INFO
	cat $(main).log
else
	rubber-info $(main).log | ccze -m ansi
endif

clean: clean_papers clean_thesis

cleanall: clean
	$(call cprint,"cleaning generated ps,dvi,pdf,paper.tex,pandoc.tex")
	@rm -f  *.{ps,dvi,pdf,pandoc.tex}
	@rm -f paper*/paper.tex

clean_minted:
	$(call cprint,"cleaning minted")
	@rm -rf _minted-$(main) $(paper)/_minted-*

clean_thesis:
	$(call cprint,"cleaning thesis")
	@rm -f *.{aux,toc,log,out,bbl,bcf,blg,pls,psm,synctex.gz,fls,fdb_latexmk,run.xml}

clean_papers:
	$(call cprint,"cleaning papers")
	@rm -f paper*/*.{aux,bbl,blg,fls,fdb_latexmk,log,out,synctex.gz}

todo:
	@# grep -r --color=tty '%.*[Tt][Oo][Dd][Oo]:'
	@ack '%.*[Tt][Oo][Dd][Oo]:'

opentex:
	$(VIM) $(chapter).tex $(VIM_FLAGS) 2> /dev/null &

openpdf:
	zathura $(chapter).pandoc.pdf &

openmkdwn:
	$(VIM) $(chapter).md $(VIM_FLAGS)

watch:
	$(call cprint,"watching for changes")
	watchmedo \
		shell-command \
		--patterns="*.tex;*.md"  \
		--command='make -j' \
		--drop
		# log \
		# --command='echo "$${watch_src_path}"' \

doit: opentex openpdf watch
# doit: $(chapter).pandoc.pdf openpdf openmkdwn
