#!/usr/bin/env python

import sys, os, logging, urllib, datetime
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
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

output = s+' '+fetchtemp()+' '+str(temperature)+' '+str(humidity)+'\n'

print(output)

with open('/home/pi/Documents/plottemp/tempdata.dat', 'a') as f:
	f.write(output)
