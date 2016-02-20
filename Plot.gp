reset

set yrange[0:100]
set mytics 10
set datafile separator ","
set xlabel "Data points"
set ylabel "Analog Input [mV]"
set timestamp "%B %d %Y %H:%M" top
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S:%f"
set format x "%Y-%m-%d %H:%M:%S:%f"

set xtics rotate # crucial line
set grid
plot 'myCANData1.dat' every ::1 using 1:2 lt 1 lw 2 title "AIN0" with lines

set terminal png
set output "/var/lib/cloud9/CAN_BBB/myPlot2.png"
replot
pause 100