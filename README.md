# 🚦 Semáforo com MicroPython

Projeto básico de semáforo utilizando **MicroPython** com a **placa ESP32/ESP8266** e 3 LEDs (verde, amarelo e vermelho).

O código simula o funcionamento de um semáforo, com tempos específicos para cada cor.

---

## 📷 Imagem do projeto

<img width="1338" height="709" alt="Captura de tela 2025-08-05 135655" src="https://github.com/user-attachments/assets/f52d23e3-9006-4e56-af4f-76d10f9a100b" />

---

## 🎯 Funcionamento

- 🟢 LED verde liga por **20 segundos**
- 🟡 LED amarelo liga por **10 segundos**
- 🔴 LED vermelho liga por **7 segundos**
- Entre cada troca, tem uma **pausa de 0.5 segundos**

---

## 🧰 Materiais usados

- 1x Placa **ESP32** (ou ESP8266)
- 3x LEDs (Verde, Amarelo, Vermelho)
- 3x Resistores (220Ω)
- Jumpers
- Protoboard

---

## 💻 Código

```python
from machine import Pin
from utime import sleep

ledRed = Pin(0, Pin.OUT)
ledYellow = Pin(2, Pin.OUT)
ledGreen = Pin(15, Pin.OUT)

while True:
    print("Ligando LED Verde...")
    ledGreen.value(1)
    sleep(20)
    print("Desligando LED Verde...")
    ledGreen.value(0)
    sleep(0.5)

    print("Ligando LED Amarelo...")
    ledYellow.value(1)
    sleep(10)
    print("Desligando LED Amarelo...")
    ledYellow.value(0)
    sleep(0.5)

    print("Ligando LED Vermelho...")
    ledRed.value(1)
    sleep(7)
    print("Desligando LED Vermelho...")
    ledRed.value(0)
    sleep(0.5)
