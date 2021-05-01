set term png
set xdata time
set timefmt '%Y-%m-%d'
seconds_per_year=365*24*60*60
set xtics 1*seconds_per_year 
plot 'result.tsv' using 1:2 title column with lines, 'result.tsv' using 1:3 title column with lines
