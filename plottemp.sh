#!/bin/bash
echo "set terminal png size 900, 300 
set xdata time
set xrange [ time(0) - 86400 : time(0) ]    # 86400 sec = 1 day
set timefmt '%Y-%m-%d,%H:%M:%S'
set format x '%H:%M'
set output '/home/pi/Documents/plottemp/images/plotinternal.png' 
plot '/home/pi/Documents/plottemp/tempdata.dat' using 1:2 w lines " | gnuplot
echo "set terminal png size 900, 300 
set xdata time
set xrange [ time(0) - 86400 : time(0) ]    # 86400 sec = 1 day
set timefmt '%Y-%m-%d,%H:%M:%S'
set format x '%H:%M'
set output '/home/pi/Documents/plottemp/images/plotexternal.png' 
plot '/home/pi/Documents/plottemp/tempdata.dat' using 1:3 w lines " | gnuplot
echo "set terminal png size 900, 300 
set xdata time
set xrange [ time(0) - 86400 : time(0) ]    # 86400 sec = 1 day
set timefmt '%Y-%m-%d,%H:%M:%S'
set format x '%H:%M'
set output '/home/pi/Documents/plottemp/images/plothumidity.png' 
plot '/home/pi/Documents/plottemp/tempdata.dat' using 1:4 w lines " | gnuplot
