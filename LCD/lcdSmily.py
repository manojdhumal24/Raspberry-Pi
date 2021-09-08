import RPi.GPIO as GPIO
from RPLCD import CharLCD, cleared, cursor
import time
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

lcd = CharLCD(cols=16, rows=2, pin_rs=7, pin_e=8, pins_data=[25, 24, 23, 18],numbering_mode=GPIO.BCM)
lcd.clear()

smiley = (
    0b00000,
    0b01010,
    0b01010,
    0b00000,
    0b10001,
    0b10001,
    0b01110,
    0b00000,
)
lcd.create_char(0, smiley)
lcd.write_string(chr(0))
time.sleep(1)
