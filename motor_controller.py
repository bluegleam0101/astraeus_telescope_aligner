import RPi.GPIO as GPIO
import time
from RpiMotorLib import RpiMotorLib

alt_pins = (17, 18, 27, 22)
direction= 16 
step = 23 
EN_pin = 24

class TelescopeMotorController():
    def __init__(self):
        self.position = []


    class AltitudeMotor():
        def __init__(self, rpimotor_function):
            self.altitude_motor = RpiMotorLib.BYJMotor()
            self.altitude_motor.motor_run(gpiopins=alt_pins, wait=.003, steps=1536, ccwise=False,
                    verbose=False, steptype="full", initdelay=.001)




    class AzimuthMotor():
        def __init__(self, rpimotor_function, gpiopins, steps_360, inv=False, wait=0.003, gear_ratio=1, steptype="full"):
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
            #finding delta degrees
            a = target_az - self.current_position
            a = (a + 180) % 360 - 180
            self.degrees_to_turn = a
            
        
            print(degrees_to_turn)
            #####################
        #moving motor



        #self.rpimotor_function()



###########################s
# Actual motor control

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(EN_pin, GPIO.OUT)
#x = 0
#for i in range(0,2):
#    GPIO.output(EN_pin, GPIO.LOW)  #s pull enable to low to enable motor
 #   mymotortest.motor_go(False,  # True=Clockwise, False=Counter-Clockwise
  #                          "Full",  # Step type (Full,Half,1/4,1/8,1/16,1/32)
   #                         200,  # number of steps
    #                        .0005,  # step delay [sec]
     #                       False,  # True = print verbose output
      #                      .05)  # initial delay [sec]
    #time.sleep(5)

    
#GPIO.cleanup()  # clear GPIO allocations after run
#skskksksksk