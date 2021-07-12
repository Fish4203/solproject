from models import *
import ramdom

def systemGen(name, seed):
    system = System(name=name, seed=name)

    random.seed = system.seed

    tempVal = random.randint(2)

    if tempVal = 1:
        # unery system with one star

        system.stars.add(starGen())

        for i in range(0, random.randint(10)):
            # how many planets are going to be gened
            system.planets.add(planetGen())
    elif tempVal = 2:
        # binery system with 2 star

        system.stars.add(starGen())
        system.stars.add(starGen())

        for i in range(0, random.randint(10)):
            # how many planets are going to be gened
            system.planets.add(planetGen())



def generate(self, name, seed):
    self.name = name
    self.seed = seed
    random.seed = seed

    t_val = random.random()  # Temp variable

    if t_val <= 0.0000003:
        self.starClass = 'O'
        self.mass = random.randrange(160000, 320000)  # *10^26 kilograms
        self.radius = self.mass * 0.4125  # In Solar radii (6.975*10^5km)
        self.temperature = math.floor(4*math.pi*self.radius*self.radius * 42.6264386916 + 6666.67)  # Kelvin (many thousands) The area of the sun multiplies by the gradient of the relationship between area and termperate for its class
    elif 0.0000003 < t_val <= 0.0013003:
        self.starClass = 'B'
        self.mass = random.randrange(21000, 160000)  # *10^26 kilograms
        self.radius = self.mass * 0.345323741007 + 1.47842  # In Solar radii (6.975*10^5km)
        self.temperature = math.floor(4*math.pi*self.radius*self.radius * 39.4729521557 + 8392.86)
    elif 0.0013003 < t_val <= 0.0073003:
        self.starClass = 'A'
        self.mass = random.randrange(14000, 21000)  # *10^26 kilograms
        self.radius = self.mass * 0.571428571429 + 0.6  # In Solar radii (6.975*10^5km)
        self.temperature = math.floor(4*math.pi*self.radius*self.radius * 155.424749113 + 3671.88)
    elif 0.0073003 < t_val <= 0.0373003:
        self.starClass = 'F'
        self.mass = random.randrange(10400, 14000)  # *10^26 kilograms
        self.radius = self.mass * 0.694444444444 + 1.58333  # In Solar radii (6.975*10^5km)
        self.temperature = math.floor(4*math.pi*self.radius*self.radius * 187.24110952 + 2888.24)
    elif 0.0373003 < t_val <= 0.1133:
        self.starClass = 'G'
        self.mass = random.randrange(8000, 10400)  # *10^26 kilograms
        self.radius = self.mass * 0.791666666667 + 0.326667  # In Solar radii (6.975*10^5km)
        self.temperature = math.floor(4*math.pi*self.radius*self.radius * 158.797648383 + 3360.94)
    elif 0.1133 < t_val <= 0.2343:
        self.starClass = 'K'
        self.mass = random.randrange(4500, 8000)  # *10^26 kilograms
        self.radius = self.mass * 1.34615384615 + 0.365714  # In Solar radii (6.975*10^5km)
        self.temperature = math.floor(4*math.pi*self.radius*self.radius * 276.56674541 + 1997.03)
    else:
        self.starClass = 'M'
        self.mass = random.randrange(800, 4500)  # *10^26 kilograms
        self.radius = self.mass * 1.75675675676 + -0.77973  # In Solar radii (6.975*10^5km)
        self.temperature = math.floor(4*math.pi*self.radius*self.radius * 212.206590789 + 2393.33)

    self.orbit = '0'
    self.orbitRadius = 0




def generate(self, name, seed, lumen, minOrbit, ismoon=False):

    # how can we estamate the temprature / solar radeation a planet recieves in a solar system?
    # how can we aproxemate atmoshpears?
    # how can we create a distrobution of planets in a semi acurate way

    self.name = name
    self.seed = seed
    random.seed = seed


    if minimum_orbit == 0 or minimum_orbit < 0 or minimum_orbit is None:
        minimum_orbit = central_body.radius * 1.05 + 0.5*central_body.radius
    self.radius = random.randrange(minimum_orbit, central_body.mass * 1000000000000000000000000000)  # In Solar radii (6.975*10^5km)  # Completely Arbitary, will need additional research but probably out of the scope of game

    t_val = random.random()
    if self.radius < central_body.radius * 300:
        if t_val <= 0.5:
            self.planetType = 'rock'
        else:
            self.planetType = 'gas'
        # Rocky or Gas (0% ice planet)
    if central_body.radius * 300 <= self.radius < central_body.radius * 700: # Semi habitable? Needs additional research
        if t_val <= 0.45:
            self.planetType = 'rock'
        elif 0.45 < t_val <= 0.8:
            self.planetType = 'gas'
        else:
            self.planetType = 'ice'
        # Rocky or Gas or ice (45% rocky, 35% gas, 20% ice
    else:
        if t_val <= 0.1:
            self.type = 'gas'
        if 0.1 < t_val <= 0.55:
            self.type = 'rock'
        else:
            self.type = 'ice'
        # Rocky or ice (~10% of gas, 45% other)
    self.axis = random.randint(0, 10)  # Planets inclination relative to the orbital plane
    self.tilt = random.randrange(0, 90)  # Planet's axis tilt in degrees from vertical
    self.planetRadius = math.floor(random.randrange(900, 0.05 * central_body.radius))  # The base radius of the planet itself in km
    if self.planetType is 'gas':
        # gassy things
        self.mass = math.floor((4/3) * math.pi * self.planetRadius**3 * random.randrange(0.9, 1.8))  # in kg
        self.atmos = None
        self.temperature = random.randint(800, 1400)  # Surface temperature  in kelvin
    if self.planetType is 'rock':
        # rocky things
        self.mass = math.floor((4/3) * math.pi * self.planetRadius**3 * random.randrange(0.8, 1.1))
        self.atmos = random.randint(0, 1)
        if self.atmos == 1:
            self.temperature = random.randint(230, 380)  # Surface temperature
        else:
            self.temperature = random.randint(125, 800)
    else:
        # icy things
        self.mass = math.floor((4/3) * math.pi * self.planetRadius**3 * random.randrange(0.9, 1.1))
        self.atmos = random.randint(0, 1)
        if self.atmos == 1:
            self.temperature = random.randint(200, 270)
        else:
            self.temperature = random.randint(125, 270)  # Surface temperature
    self.gravity = ((6.67*10**-11) * self.mass)/self.planetRadius**2  # Gravitational pull at planetRadius


    for i in random.randint(0,3):
        self.generate()
