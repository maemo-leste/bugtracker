.POSIX: 

all: clean graph.png

result.tsv:
	python3 ./import_issues.py

graph.png: result.tsv
	gnuplot plot.gnuplot > $@

clean:
	rm -f graph.png result.tsv

.PHONY: all clean
