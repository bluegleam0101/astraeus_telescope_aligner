from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd

i2c = I2C(0, sda=Pin(2), scl=Pin(3), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
while True:
    print(I2C_ADDR)

lcd.putstr("I2C Address:"+str(I2C_ADDR)+"\n")
lcd.putstr("Tom's Hardware")
sleep(2)