from models import *
import ramdom
import math


# v\left(l_{1}\sin\left(\frac{t_{1}^{2}}{a_{1}t_{2}}\right)+x_{1},h_{1}\cos\left(\frac{t_{1}^{2}}{a_{1}t_{2}}\right)+x_{2}\right)

# orbit shit
# \left(l_{1}\sin\left(\frac{\pi\cdot t_{1}^{2}}{a_{1}t_{1}a}\right)+x_{1},h_{1}\cos\left(\frac{\pi\cdot t_{1}^{2}}{a_{1}t_{1}a}\right)+x_{2}\right)
# x = L * Sin(pi * t^2 / p * t * a) + x
# y = H * Cos(pi * t^2 / p * t * a) + y


def systemGen(name, seed):
    system = System(name=name, seed=name)

    random.seed = system.seed

    tempVal = random.randint(2)

    if tempVal = 1:
        # unery system with one star

        system.stars.add(starGen(name= name+'a', str(random.random())))

        for i in range(0, random.randint(10)):
            # how many planets are going to be gened
            system.planets.add(planetGen())


    elif tempVal = 2:
        # binery system with 2 star

        system.stars.add(starGen())
        system.stars.add(starGen())
        # todo: orbit shit

        for i in range(0, random.randint(10)):
            # how many planets are going to be gened
            system.planets.add(planetGen())



def starGen(name, seed):
    # this should be mostly done and working for unery systems
    star = Star(name=name, seed=seed)
    random.seed = star.seed

    t_val = random.random()  # Temp variable

    if t_val <= 0.0000003:
        star.starClass = 'O'
        star.mass = random.randrange(160000, 320000)  # *10^26 kilograms
        star.radius = star.mass * 0.4125  # In Solar radii (6.975*10^5km)
        star.temperature = math.floor(4*math.pi*star.radius*star.radius * 42.6264386916 + 6666.67)  # Kelvin (many thousands) The area of the sun multiplies by the gradient of the relationship between area and termperate for its class
    elif 0.0000003 < t_val <= 0.0013003:
        star.starClass = 'B'
        star.mass = random.randrange(21000, 160000)  # *10^26 kilograms
        star.radius = star.mass * 0.345323741007 + 1.47842  # In Solar radii (6.975*10^5km)
        star.temperature = math.floor(4*math.pi*star.radius*star.radius * 39.4729521557 + 8392.86)
    elif 0.0013003 < t_val <= 0.0073003:
        star.starClass = 'A'
        star.mass = random.randrange(14000, 21000)  # *10^26 kilograms
        star.radius = star.mass * 0.571428571429 + 0.6  # In Solar radii (6.975*10^5km)
        star.temperature = math.floor(4*math.pi*star.radius*star.radius * 155.424749113 + 3671.88)
    elif 0.0073003 < t_val <= 0.0373003:
        star.starClass = 'F'
        star.mass = random.randrange(10400, 14000)  # *10^26 kilograms
        star.radius = star.mass * 0.694444444444 + 1.58333  # In Solar radii (6.975*10^5km)
        star.temperature = math.floor(4*math.pi*star.radius*star.radius * 187.24110952 + 2888.24)
    elif 0.0373003 < t_val <= 0.1133:
        star.starClass = 'G'
        star.mass = random.randrange(8000, 10400)  # *10^26 kilograms
        star.radius = star.mass * 0.791666666667 + 0.326667  # In Solar radii (6.975*10^5km)
        star.temperature = math.floor(4*math.pi*star.radius*star.radius * 158.797648383 + 3360.94)
    elif 0.1133 < t_val <= 0.2343:
        star.starClass = 'K'
        star.mass = random.randrange(4500, 8000)  # *10^26 kilograms
        star.radius = star.mass * 1.34615384615 + 0.365714  # In Solar radii (6.975*10^5km)
        star.temperature = math.floor(4*math.pi*star.radius*star.radius * 276.56674541 + 1997.03)
    else:
        star.starClass = 'M'
        star.mass = random.randrange(800, 4500)  # *10^26 kilograms
        star.radius = star.mass * 1.75675675676 + -0.77973  # In Solar radii (6.975*10^5km)
        star.temperature = math.floor(4*math.pi*star.radius*star.radius * 212.206590789 + 2393.33)




def planetGen(name, seed, lumen, minOrbit, maxOrbit, ismoon=False):

    # how can we estamate the temprature / solar radeation a planet recieves in a solar system?
    # how can we aproxemate atmoshpears?
    # how can we create a distrobution of planets in a semi acurate way

    planet = Planet(name=name, seed=seed)

    random.seed = planet.seed

    planet.axis = random.randint(0, 10)  # Planets inclination relative to the orbital plane
    planet.tilt = random.randrange(0, 90)  # Planet's axis tilt in degrees from vertical

    if ismoone:
        # idk about moon stuff
        pass
    else:
        t_val = random.random()

        if t_val <= 0.3:
            planet.type = 'gas'
            planet.mass = random.range(2.35938*(10**25), 6.86655*(10**26)) # Exoplanet data Units: kg
            planet.radius = 5.4 * (10**-16)* (planet.mass**0.441) # baised on exoplanet data extrapolation Units: AU

            # orbit shit
            orbit = Orbit()
            orbit.a = random.range(0.052995525, 0.231969) # baised on 1, 3ed quartiles of the exoplanet data Units: AU
            orbit.ecentricity = random.range(0, 0.042) # baised on 1, 3ed quartiles of the exoplanet data
            orbit.b = math.sqrt((orbit.a**2) - (orbit.a**2) * (orbit.ecentricity**2)) # using a derived vertion of this formular e == Sqrt[1 - b^2/a^2] Units: AU
            orbit.p = (orbit.b**2) / orbit.a # using this formular p=\frac{b^{2}}{a}
            orbit.BigM = bigM # mass of the centrial body Units: kg
            orbit.rotation = random.range(0, 360) # the rotation aroung the plane Units: deg
            orbit.period = 2*math.pi* math.sqrt(((orbit.a * 149597900000) ** 3) / (orbit.BigM * 6.674 * (10**-11))) # the period of orbit baised on Units: s (seconds)
            orbit.save()

            planet.orbit = orbit

        if 0.3 < t_val <= 0.7:
            planet.type = 'rock'
            planet.mass = random.range(3.301*(10**23), 5.972*(10**24)) # Our solarsystem data Units: kg
            planet.radius = 5.4 * (10**-16)* (planet.mass**0.441)  # baised on exoplanet data extrapolation Units: AU


            # orbit shit
            orbit = Orbit()
            orbit.a = random.range(0.052995525, 0.231969) # baised on 1, 3ed quartiles of the exoplanet data Units: AU
            orbit.ecentricity = random.range(0, 0.042) # baised on 1, 3ed quartiles of the exoplanet data
            orbit.b = math.sqrt((orbit.a**2) - (orbit.a**2) * (orbit.ecentricity**2)) # using a derived vertion of this formular e == Sqrt[1 - b^2/a^2] Units: AU
            orbit.p = (orbit.b**2) / orbit.a # using this formular p=\frac{b^{2}}{a}
            orbit.BigM = bigM # mass of the centrial body Units: kg
            orbit.rotation = random.range(0, 360) # the rotation aroung the plane Units: deg
            orbit.period = 2*math.pi* math.sqrt(((orbit.a * 149597900000) ** 3) / (orbit.BigM * 6.674 * (10**-11))) # the period of orbit baised on Units: s (seconds)
            orbit.save()

            planet.orbit = orbit

        else:
            planet.type = 'ice'
            planet.mass = random.range(8.682*(10**25), 1.024*(10**26)) # Exoplanet data Units: kg
            planet.radius = 5.4 * (10**-16)* (planet.mass**0.441)  # baised on exoplanet data extrapolation Units: AU


            # orbit shit
            orbit = Orbit()
            orbit.a = random.range(0.052995525, 0.231969) # baised on 1, 3ed quartiles of the exoplanet data Units: AU
            orbit.ecentricity = random.range(0, 0.042) # baised on 1, 3ed quartiles of the exoplanet data
            orbit.b = math.sqrt((orbit.a**2) - (orbit.a**2) * (orbit.ecentricity**2)) # using a derived vertion of this formular e == Sqrt[1 - b^2/a^2] Units: AU
            orbit.p = (orbit.b**2) / orbit.a # using this formular p=\frac{b^{2}}{a}
            orbit.BigM = bigM # mass of the centrial body Units: kg
            orbit.rotation = random.range(0, 360) # the rotation aroung the plane Units: deg
            orbit.period = 2*math.pi* math.sqrt(((orbit.a * 149597900000) ** 3) / (orbit.BigM * 6.674 * (10**-11))) # the period of orbit baised on Units: s (seconds)
            orbit.save()

            planet.orbit = orbit

        planet.gravity = ((6.67*10**-11) * planet.mass)/planet.planetRadius**2  # Gravitational pull at planetRadius