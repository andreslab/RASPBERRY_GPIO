import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT) #pin en modo de salida

while True:
    GPIO.output(7, True) #encendido
    time.sleep(1)
    GPIO.output(7, False) #apagado
    time.sleep(1)
