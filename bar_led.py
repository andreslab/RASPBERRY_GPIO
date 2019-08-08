import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT, initial = 0) #inicializamos los pines en apagado
GPIO.setup(13, GPIO.OUT, initial = 0) #inicializar los pines ya definidos

while True:
    GPIO.output(7, 1) #1 : True
    sleep(1)
    GPIO.output(7,0) #0 : False
    sleep(1)
