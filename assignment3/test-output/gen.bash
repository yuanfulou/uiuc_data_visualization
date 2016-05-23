#!/bin/bash
dot -Tpdf amazon.gv -o ad.pdf
neato -Tpdf amazon.gv -o an.pdf
twopi -Tpdf amazon.gv -o at.pdf
circle -Tpdf amazon.gv -o ac.pdf
fdp -Tpdf amazon.gv -o af.pdf
sfdp -Tpdf amazon.gv -o as.pdf
patchwork -Tpdf amazon.gv -o ap.pdf
