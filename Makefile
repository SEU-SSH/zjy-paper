TEX := main.tex
PDF := main.pdf
BIB := refs.bib

TECTONIC ?= tectonic
D2 ?= d2
RSVG_CONVERT ?= rsvg-convert

FIGURE_SOURCES := $(wildcard figures/src/*.d2)
FIGURE_PDFS := $(patsubst figures/src/%.d2,figures/%.pdf,$(FIGURE_SOURCES))
FIGURE_SVGS := $(patsubst figures/src/%.d2,figures/%.svg,$(FIGURE_SOURCES))
MANUSCRIPT_FIGURES := $(wildcard figures/*.pdf)

.DEFAULT_GOAL := pdf

.PHONY: all pdf figures figures-pdf figures-svg verify clean distclean help

all: pdf

pdf: $(PDF) ## Build the paper PDF

$(PDF): $(TEX) $(BIB) $(MANUSCRIPT_FIGURES)
	$(TECTONIC) $(TEX)

figures: figures-pdf figures-svg ## Rebuild all figures from D2 sources

figures-pdf: $(FIGURE_PDFS)

figures-svg: $(FIGURE_SVGS)

figures/%.pdf: figures/%.svg
	$(RSVG_CONVERT) --format=pdf1.5 --output=$@ $<

figures/%.svg: figures/src/%.d2
	$(D2) $< $@

verify: pdf ## Build and inspect the resulting PDF
	pdfinfo $(PDF)

clean: ## Remove temporary LaTeX files
	$(RM) main.aux main.bbl main.blg main.log main.out main.synctex.gz main.toc main.lof main.lot

distclean: clean ## Remove the generated paper PDF
	$(RM) $(PDF)

help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  %-14s %s\n", $$1, $$2}'
