#!/usr/bin/env python

#Aplicacion para adquirir la temperatura de la raspberry, y del sen
#sensor DHT11 (no dispone de decimales)

import sys, os, logging, urllib, datetime
import Adafruit_DHT

#opciones Adafruit_DHT.DHT11/Adafruit_DHT.DHT22 
sensor = Adafruit_DHT.DHT11 #modelo actual instalado en la raspberry.
pin = 17 #pin 11 ->GPIO17

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

def fetchtemp():
	cmd = '/opt/vc/bin/vcgencmd measure_temp'
	line = os.popen(cmd).readline().strip()
	output = line.split('=')[1].split("'")[0]#+' C'
	return output 

format = "%Y-%m-%d,%H:%M:%S" 
today = datetime.datetime.today()
s = today.strftime(format)

#datos que quedaran registrados en el fichero tempdata.dat
output = s+' '+fetchtemp()+' '+str(temperature)+' '+str(humidity)+'\n'

print(output)
#escritura en el fichero.
with open('/home/pi/Documents/plottemp/tempdata.dat', 'a') as f:
	f.write(output)
