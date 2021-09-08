import RPi.GPIO as GPIO
from RPLCD import CharLCD
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
lcd = CharLCD(cols=16, rows=2, pin_rs=7, pin_e=8, pins_data=[25, 24, 23, 18],numbering_mode=GPIO.BCM)

while True:
    lcd.write_string(u"Hello world!")
    time.sleep(1)
    lcd.clear()
    time.sleep(1)
