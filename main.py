import time
import csv
import gpiozero
from datetime import datetime
import astropy.units as units
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from motor_controller import TelescopeMotorController


ts = load.timescale()
t = ts.now()

planets = load('de440s.bsp')
earth = planets['earth']

class TelescopePointer:
    def __init__(self, telescope_motor_api):
        self.earth = planets['earth']
        self.target: object

    def set_target(self, query, latlng):
        """gets current ra, dec, distance, altitude and azimuth for a celestial object specified by the 'celestial_body' parameter,
         sets target. target astrometrics (ra, dec) given in floating point numbers which are degrees"""
        time = Time(datetime.now()) 
        geo_location = EarthLocation(lat=latlng[0]*units.deg, lon=latlng[0]*units.deg, height=5*units.m)
        self.target = SkyCoord.from_name(query)
        self.target = self.target.transform_to(AltAz(obstime=time,location=geo_location))
        print(self.target.az, self.target.alt, self.target.info)
        print(
            #f"right inclination axis: {self.target['ra']} degrees\n"
            #f"declination axis: {self.target['dec']} degrees\n"
            #f"distance: {self.target['dis']}\n"
            f"local altitude: {self.target.alt}\n"
            f"local azimuth: {self.target.az}\n"
        )






##initializing classes and subclasses##


telescope_motor_api = TelescopeMotorController()

az_motor = telescope_motor_api.AzimuthMotor(rpimotor_function=RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825"), gpiopins="bonjupr",steps_360=200)
alt_motor = telescope_motor_api.AltitudeMotor()
pointer = TelescopeInterface(altitudemotor_fm=alt_motor, azimuthmotor_fm=az_motor)







######main program#######

    # align func is a function you have to pass that takes a ra- and dec axis and points the telescopes

    def align(self, ra, dec, telescope_motor_api, continuous=False, continuous_interval=10):
        """
        Aligns telescope by calling upon the telescope_motor_api function (that you have to create yourself).

        takes ra and dec, both in degrees.

        Set continuous to True if you want to keep aligning at an interval of 10 seconds. (10 is default but can be
        changed using the continuous_interval parameter)
        """
        if not continuous:
            telescope_motor_api(self.target['ra'], self.target['dec'])
            print("aligning was successful")

        if continuous:
            print("continuously aligning...\nssss")
            while True:
                telescope_motor_api(ra=self.ra, dec=self.dec)
                print('aligned')
                time.sleep(continuous_interval)

    def display_text(self, text):
        pass


pointer = TelescopePointer(pi_controller)

if __name__ == "__main__":
    while True:
        latlng = geocoder.ip('me').latlng
        print(f"Current coordinates: lat: {latlng[0]}, long: {latlng[1]}.")
        if latlng is None:
            print("Could not get current coordinates.")
            current_long = str.title(input("please specify your longitude: "))
            current_lat = str.title(input("please specify your latitude: "))
            latlng = [current_lat, current_long]

        choice = input("would you like to set a new target or align telescope? (S/A): ")

        if choice == 'S':
            for i in range(1, 100):
                try:
                    pointer.set_target(query=input("Please enter celestial object to set as target: "), latlng=latlng)
                    print("target set, ready to align")
                except ValueError:
                    print("Celestial object not found, please try again.")
                    continue
                break

        elif choice == 'A':
            continuous = bool(int(input("Continuous align? 1 for yes, 0 for no: ")))
            pointer.align(
                ra=pointer.target['ra'],
                dec=pointer.target['dec'],
                continuous=continuous,
                telescope_motor_api=pi_controller()
            )

    # pointer.align(dgbsdhfb