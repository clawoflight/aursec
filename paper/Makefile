.PHONY: all clean

aursec.pdf: img/*.png img/*.jpg detailedDescription/*.tex *.tex Literature.bib
	latexmk -lualatex -latexoption=-shell-escape -f aursec.tex

img/state-diagram.dot.png: img/state-diagram.dot
	dot -Tpng $< -o $@

clean:
	latexmk -c
	rm -vf *.dvi *.log *.bbl
