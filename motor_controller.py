import RPi.GPIO as GPIO
import time
from RpiMotorLib import RpiMotorLib

#in1 = 17
#in2 = 18s
#in3 = 27
#in4 = 22

direction= 22 # Direction (DIR) GPIO Pin
step = 23 # Step GPIO Pin
EN_pin = 24 # enable motor if output = low

# Declare a instance of class pass GPIO pins numbers and the motor type
mymotortest = RpiMotorLib.A4988Nema(direction, step, (21, 21, 21), "DRV8825")
GPIO.setup(EN_pin, GPIO.OUT)  # set enable pin as output

###########################
# Actual motor control
###########################
#
x = 0

GPIO.output(EN_pin, GPIO.LOW)  #s pull enable to low to enable motor
mymotortest.motor_go(False,  # True=Clockwise, False=Counter-Clockwise
                        "Full",  # Step type (Full,Half,1/4,1/8,1/16,1/32)
                        200,  # number of steps
                        .0005,  # step delay [sec]
                        False,  # True = print verbose output
                        .05)  # initial delay [sec]
time.sleep(5)
GPIO.cleanup()  # clear GPIO allocations after run