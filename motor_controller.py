import RPi.GPIO as GPIO
import time
from RpiMotorLib import RpiMotorLib

alt_pins = (17, 18, 27, 22)
#direction= 16 
#step = 23 
#EN_pin = 24

class altitude_motor():
    def __init__(self, rpimotor_function)
altitude_motor = RpiMotorLib.BYJMotor()
altitude_motor.motor_run(gpiopins=alt_pins, wait=.003, steps=1536, ccwise=False,
                  verbose=False, steptype="full", initdelay=.001)




class azimuth_motor():
    def __init__(self, rpimotor_function, gpiopins, steps_360, inv=False wait=0.003, gear_ratio=1, steptype="full"):
        '''
        please provide gear ratio as a float corresponding to
        the amount of times to motor has to turn 360° to fully
        rotate to telescope once.
          
        the steps_360 parameter asks for the amount of steps your stepper motor has to turn to turn 360° in full step mode
        '''
        self.name = rpimotor_function.name
        self.current_position = 0.0
        self.rpimotor_function = rpimotor_function
        self.ccwise = False
        self.degrees_to_turn: float

    def align_azimuth(self, target_az):
        self.delta_degrees = self.current_position - target_az
        if self.delta_degrees <= 0:
            
            self.degrees_to_turn = (self.current_position - target_az)

        elif (self.current_position - target_az) >= 180:




        self.rpimotor_function()




###########################
# Actual motor control

#x = 0
#for i in range(0,2):
    #GPIO.output(EN_pin, GPIO.LOW)  #s pull enable to low to enable motor
    #mymotortest.motor_go(False,  # True=Clockwise, False=Counter-Clockwise
                            #"Full",  # Step type (Full,Half,1/4,1/8,1/16,1/32)
                            #200,  # number of steps
                            #.0005,  # step delay [sec]
                            #False,  # True = print verbose output
                            #.05)  # initial delay [sec]
    #time.sleep(5)

    
GPIO.cleanup()  # clear GPIO allocations after run
#skskksksksk