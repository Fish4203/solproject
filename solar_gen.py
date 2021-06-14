# Revision 1.0    // PLEASE MAKE A COPY AND EDIT BEFORE MAKING CHANGES

import random
import math


class Sun:
    def __init__(self, seed):
        self.name = ""
        self.id = seed  # int
        self.star_class = ''  # Letter O, B, A, F, G, K, M
        self.mass = None  # int, *10^26 kilograms
        self.temperature = None  # Int, degrees kelvin
        self.radius = None  # int, kilometers

        random.seed = self.id
        t_val = random.random()  # Temp variable
        if t_val <= 0.0000003:
            self.star_class = 'O'
            self.mass = random.randrange(160000, 320000)  # *10^26 kilograms
            self.radius = self.mass * 0.4125  # In Solar radii (6.975*10^5km)
            self.temperature = math.floor(4*math.pi*self.radius*self.radius * 42.6264386916 + 6666.67)  # Kelvin (many thousands) The area of the sun multiplies by the gradient of the relationship between area and termperate for its class
        elif 0.0000003 < t_val <= 0.0013003:
            self.star_class = 'B'
            self.mass = random.randrange(21000, 160000)  # *10^26 kilograms
            self.radius = self.mass * 0.345323741007 + 1.47842  # In Solar radii (6.975*10^5km)
            self.temperature = math.floor(4*math.pi*self.radius*self.radius * 39.4729521557 + 8392.86)
        elif 0.0013003 < t_val <= 0.0073003:
            self.star_class = 'A'
            self.mass = random.randrange(14000, 21000)  # *10^26 kilograms
            self.radius = self.mass * 0.571428571429 + 0.6  # In Solar radii (6.975*10^5km)
            self.temperature = math.floor(4*math.pi*self.radius*self.radius * 155.424749113 + 3671.88)
        elif 0.0073003 < t_val <= 0.0373003:
            self.star_class = 'F'
            self.mass = random.randrange(10400, 14000)  # *10^26 kilograms
            self.radius = self.mass * 0.694444444444 + 1.58333  # In Solar radii (6.975*10^5km)
            self.temperature = math.floor(4*math.pi*self.radius*self.radius * 187.24110952 + 2888.24)
        elif 0.0373003 < t_val <= 0.1133:
            self.star_class = 'G'
            self.mass = random.randrange(8000, 10400)  # *10^26 kilograms
            self.radius = self.mass * 0.791666666667 + 0.326667  # In Solar radii (6.975*10^5km)
            self.temperature = math.floor(4*math.pi*self.radius*self.radius * 158.797648383 + 3360.94)
        elif 0.1133 < t_val <= 0.2343:
            self.star_class = 'K'
            self.mass = random.randrange(4500, 8000)  # *10^26 kilograms
            self.radius = self.mass * 1.34615384615 + 0.365714  # In Solar radii (6.975*10^5km)
            self.temperature = math.floor(4*math.pi*self.radius*self.radius * 276.56674541 + 1997.03)
        else:
            self.star_class = 'M'
            self.mass = random.randrange(800, 4500)  # *10^26 kilograms
            self.radius = self.mass * 1.75675675676 + -0.77973  # In Solar radii (6.975*10^5km)
            self.temperature = math.floor(4*math.pi*self.radius*self.radius * 212.206590789 + 2393.33)


class Planet:
    def __init__(self, seed, minimum_orbit, central_body):
        self.radius = None  # Orbit radius
        self.p_type = None
        self.id = seed
        self.orbital_speed = None  # How long it takes to orbit central body
        self.axis = None  # Planets inclination relative to the orbital plane
        self.p_axis = None  # Planet's axis tilt
        self.moons = None
        self.atmosphere = None
        self.temperature = None  # Surface temperature
        self.mass = None
        self.p_radius = None  # The base radius of the planet itself
        self.gravity = None  # Gravitational pull at p_radius
        if minimum_orbit == 0 or minimum_orbit < 0 or minimum_orbit is None:
            minimum_orbit = central_body.radius * 1.05 + 0.5*central_body.radius
        self.radius = random.randrange(minimum_orbit, central_body.mass * 1000000000000000000000000000)  # In Solar radii (6.975*10^5km)  # Completely Arbitary, will need additional research but probably out of the scope of game
        random.seed = self.id
        t_val = random.random()
        if self.radius < central_body.radius * 300:
            if t_val <= 0.5:
                self.p_type = 'rock'
            else:
                self.p_type = 'gas'
            # Rocky or Gas (0% ice planet)
        if central_body.radius * 300 <= self.radius < central_body.radius * 700: # Semi habitable? Needs additional research
            if t_val <= 0.45:
                self.p_type = 'rock'
            elif 0.45 < t_val <= 0.8:
                self.p_type = 'gas'
            else:
                self.p_type = 'ice'
            # Rocky or Gas or ice (45% rocky, 35% gas, 20% ice
        else:
            if t_val <= 0.1:
                self.type = 'gas'
            if 0.1 < t_val <= 0.55:
                self.type = 'rock'
            else:
                self.type = 'ice'
            # Rocky or ice (~10% of gas, 45% other)
        self.orbital_speed = (2*math.pi*math.sqrt(self.radius*self.radius*self.radius))/(math.sqrt(6.67*10**-11)*math.sqrt(central_body.mass))  # How long it takes to orbit central body
        self.axis = random.randint(0, 10)  # Planets inclination relative to the orbital plane
        self.p_axis = random.randrange(0, 90)  # Planet's axis tilt in degrees from vertical
        self.p_radius = math.floor(random.randrange(900, 0.05 * central_body.radius))  # The base radius of the planet itself in km
        if self.p_type is 'gas':
            # gassy things
            self.mass = math.floor((4/3) * math.pi * self.p_radius**3 * random.randrange(0.9, 1.8))  # in kg
            self.atmosphere = None
            self.temperature = random.randint(800, 1400)  # Surface temperature  in kelvin
        if self.p_type is 'rock':
            # rocky things
            self.mass = math.floor((4/3) * math.pi * self.p_radius**3 * random.randrange(0.8, 1.1))
            self.atmosphere = random.randint(0, 1)
            if self.atmosphere == 1:
                self.temperature = random.randint(230, 380)  # Surface temperature
            else:
                self.temperature = random.randint(125, 800)
        else:
            # icy things
            self.mass = math.floor((4/3) * math.pi * self.p_radius**3 * random.randrange(0.9, 1.1))
            self.atmosphere = random.randint(0, 1)
            if self.atmosphere == 1:
                self.temperature = random.randint(200, 270)
            else:
                self.temperature = random.randint(125, 270)  # Surface temperature
        self.gravity = ((6.67*10**-11) * self.mass)/self.p_radius**2  # Gravitational pull at p_radius
        self.moons = {}
        for m in range(0, random.randint(0, 3)):
            self.moons[m] = Planet(self.id + 1, self.p_radius * 1.2, self)

