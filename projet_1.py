# projet_1.py

from time import *

# lcd sur D1=5, D2=4
import qliic_i2clcd
lcd = qliic_i2clcd.LCD(2, 16)

# potentiometre sur A0
from machine import ADC
pot = ADC(0)

# bouton sur D6=12
BOUTON_PIN = 12 
pin_d7 = machine.Pin(BOUTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

# RGB sur D3=0
from qliic_neopixel import NEOPIXEL
my_neopixel = NEOPIXEL(0, 5)
my_neopixel.clear()

# init

lcd.putstr("Allo, on Qliic  ensemble ?")
sleep(1)
lcd.clear()
lcd.putstr("D2-D1:LCD D3:RGB   ")
lcd.move_to(0, 1)
lcd.putstr("A0:POT  D6:BOUT")
sleep(2)
lcd.clear()

try:
    while True:
        pot_valeur = pot.read()
        bouton = pin_d7.value()
        
        pot_str = f"{pot_valeur}    "
        lcd.move_to(0, 0)
        lcd.putstr(f"potent.: {pot_str}")
        lcd.move_to(0, 1)
        lcd.putstr(f"bouton: {bouton}")
        
        if (bouton == 0):   
            my_neopixel.set_pixel_color(0, int(pot_valeur/8), 0, 0)
            my_neopixel.show()
        else:
            my_neopixel.set_pixel_color(0, 0, 0, 0)
            my_neopixel.show()
                
        sleep_ms(100)

except KeyboardInterrupt:
        lcd.clear()
        lcd.putstr("Au revoir")


