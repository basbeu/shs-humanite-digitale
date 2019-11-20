all: rapport clean

rapport: rapport-b.tex
	pdflatex -synctex=1 -interaction=nonstopmode $^;
	pdflatex -synctex=1 -interaction=nonstopmode $^;
	pdflatex -synctex=1 -interaction=nonstopmode $^

clean:
	rm *.aux *.log *.out *.gz


