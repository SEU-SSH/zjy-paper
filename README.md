# DeFuzz Paper

This repository contains the manuscript, bibliography, figures, and supporting
notes for the DeFuzz paper. The review manuscript uses the IEEE conference
format and keeps author information anonymous.

## Build

Install [Tectonic](https://tectonic-typesetting.github.io/) and run:

```sh
make
```

The generated review manuscript is `main.pdf`. Use `make verify` to rebuild it
and display its PDF metadata.

The editable diagram sources are under `figures/src/`. Install
[D2](https://d2lang.com/) and `rsvg-convert`, then run `make figures` to
regenerate both PDF and SVG versions of every diagram before rebuilding the
manuscript. The rendered figure files are versioned, so a normal paper build
only requires Tectonic.

## Repository layout

- `main.tex`: LaTeX manuscript source
- `refs.bib`: BibTeX bibliography
- `figures/`: publication PDFs, SVG previews, and D2 sources
- `paper.md`: Markdown working draft
- `outline*.md`: outline and completion tracking
- `experiment_*.md`: experiment status and execution notes
- `DeFuzz-中文阅读版.*`: Chinese reading edition
