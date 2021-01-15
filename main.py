# -*- coding: utf-8 -*-
#!/usr/bin/python

from bottle import route, run,template, static_file
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 17

@route("/static/<filename>")
def server_static(filename):
	return static_file(filename,root="./static")

@route("/images/<filename>")
def server_static(filename):
	return static_file(filename, root="/home/pi/Documents/plottemp/images", mimetype="image/png")

@route("/")
def main():
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	templateData = {'temperature' : temperature, 'humidity' : humidity}
	print "Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity)
	return template('/home/pi/Documents/plottemp/main_bottle.html', **templateData)

run(host='0.0.0.0', port=80, debug=True)
