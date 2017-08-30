#! /usr/bin/gnuplot -persist
set term png size 1024,768
#set terminal postscript eps enhanced color size 1024, 768
set output outf
set grid
set yrange[0:]
set xdata time
set xlabel "Time"
set ylabel "Mb/s"
set timefmt "%Y-%m-%d %H:%M:%S"
set format x "%Y-%m-%d %H:%M:%S"
set xrange [] noreverse nowriteback
set xtics rotate
plot filename using 1:3 title filename  with filledcurve x1 lt 1 lc
