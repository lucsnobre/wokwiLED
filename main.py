from machine import Pin

from utime import  sleep
print("projeto cachorrada ligado")
ledGreen = Pin(15, Pin.OUT)
ledYellow = Pin(2, Pin.OUT)
ledRed = Pin(0, Pin.OUT)

while True:
    ledGreen.on()
    print("LED VERDE LIGADO!")
    sleep(20)
    ledGreen.off()
    print("LED VERDE DESLIGADO!")
    sleep(0.5)

    ledYellow.on()
    print("LED AMARELO LIGADO")
    sleep(10)
    ledYellow.off()
    print("LED AMARELO DESLIGADO!")
    sleep(0.5)

    ledRed.on()
    print("LED VERMELHO LIGADO!")
    sleep(7)
    ledRed.off()
    print("LED VERMELHO DESLIGADO")
    sleep(0.5)
