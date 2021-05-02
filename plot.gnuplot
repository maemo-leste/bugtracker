set term pngcairo enhanced font "monospace,12.0" size 1600,1080
set xdata time
set timefmt '%Y-%m-%d'
set xrange [*:*] noextend
seconds_per_year=365*24*60*60
set xtics 0.5*seconds_per_year format "%d/%b/%Y"
set grid
plot 'result.tsv' using 1:2 title column with lines, \
     'result.tsv' using 1:3 title column with lines
