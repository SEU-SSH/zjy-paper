#!/bin/bash
cd "$(dirname "$0")"
if command -v /Library/TeX/texbin/pdflatex >/dev/null 2>&1; then
  /Library/TeX/texbin/pdflatex -interaction=nonstopmode main.tex > compile.log 2>&1
elif command -v tectonic >/dev/null 2>&1; then
  tectonic main.tex > compile.log 2>&1
else
  echo "Error: Neither pdflatex nor tectonic found." >&2
  exit 1
fi
