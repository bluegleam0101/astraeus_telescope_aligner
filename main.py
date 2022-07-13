import time
import csv
import threading
import geocoder
from skyfield.api import load, Angle
from pi_motor_controller import pi_controller
from skyfield.api import N, W, wgs84

ts = load.timescale()
t = ts.now()

planets = load('de440s.bsp')
earth = planets['earth']


class TelescopePointer:
    def __init__(self, telescope_motor_api):
        self.earth = planets['earth']
        self.target = {}

    def set_target(self, celestial_body, latlng):
        """gets current ra, dec, distance, altitude and azimuth for a celestial object specified by the 'celestial_body' parameter,
         sets target. target astrometrics (ra, dec) given in floating point numbers which are degrees"""

        amersfoort = earth + wgs84.latlon(latlng[0] * N, latlng[1] * W)
        astrometric = amersfoort.at(t).observe(celestial_body)
        self.alt, self.az, self.distance = astrometric.apparent().altaz()

        astrometric = self.earth.at(t).observe(planets[celestial_body])
        self.ra, self.dec, self.distance = astrometric.radec()
        self.target = {'ra': float(self.ra.hours) * 15, 'dec': float(self.dec.degrees), 'dis': self.distance}
        print(astrometric.radec())
        print(
            f"right inclination axis: {self.target['ra']} degrees\n"
            f"declination axis: {self.target['dec']} degrees\n"
            f"distance: {self.target['dis']}\n"
            f"local altitude: {self.alt}\n"
            f"local azimuth: {self.az}\n"
        )

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
                    pointer.set_target(celestial_body=input("Please enter celestial object to set as target: "), latlng=latlng)
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