# Temperatura
Raspberry con el sensor de temperatura y humedad DHT11 (+/-1ºC)

* Temperatura interna: La temperatura de la CPU la obtiene de '/opt/vc/bin/vcgencmd measure_temp'
* Temperatura externa: Hace la lectura del sensor DHT11.
* Humedad: Lectura de humedad del senser DHT11.

# Instalación
Para que se ejecute la lectura de la temperatura cada 5 minutos.
```
Crontab -e
*/5 * * * * python3 /home/pi/plottemp/datagen.py && /home/pi/plottemp/plottemp.sh &> /dev/null
```

