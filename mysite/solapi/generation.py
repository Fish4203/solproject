from .models import *
import random
import math


# v\left(l_{1}\sin\left(\frac{t_{1}^{2}}{a_{1}t_{2}}\right)+x_{1},h_{1}\cos\left(\frac{t_{1}^{2}}{a_{1}t_{2}}\right)+x_{2}\right)

# orbit shit
# \left(l_{1}\sin\left(\frac{\pi\cdot t_{1}^{2}}{a_{1}t_{1}a}\right)+x_{1},h_{1}\cos\left(\frac{\pi\cdot t_{1}^{2}}{a_{1}t_{1}a}\right)+x_{2}\right)
# x = L * Sin(pi * t^2 / p * t * a) + x
# y = H * Cos(pi * t^2 / p * t * a) + y


def systemGen(name, seed):
    system = System(name=name, seed=seed)

    #orbit shit
    orbit = Orbit()
    orbit.a = 0
    orbit.b = 0
    orbit.p = 0
    orbit.exentricity = 0
    orbit.bigM = 0
    orbit.rotation = 0
    orbit.period = 0
    orbit.save()

    system.orbit = orbit
    system.save()

    random.seed = system.seed

    tempVal = random.randint(1,1)

    if tempVal == 1:
        # unery system with one star
        star = starGen(name= name+'star'+'a', seed=str(random.random()))
        system.stars.add(star)

        bigM = star.mass

        for i in range(0, random.randint(0,10)):
            # how many planets are going to be gened
            system.planets.add(planetGen(name=name+'planet'+str(i), seed=str(random.random()), bigM=bigM))


    elif tempVal == 2:
        # binery system with 2 star

        system.stars.add(starGen())
        system.stars.add(starGen())
        # todo: orbit shit

        for i in range(0, random.randint(0,10)):
            # how many planets are going to be gened
            system.planets.add(planetGen())



def starGen(name, seed):
    # this should be mostly done and working for unery systems
    star = Star(name=name, seed=seed)
    random.seed = star.seed

    t_val = random.random()  # Temp variable

    if t_val <= 0.0000003:
        star.starClass = 'O'
        star.mass = random.uniform(160000 * (10**26), 320000 * (10**26))  # Units: kg
        star.radius = star.mass * 0.4125  * 6.975 * (10**5)  # Units: kg
        star.temperature = math.floor(4*math.pi*star.radius*star.radius * 42.6264386916 + 6666.67)  # Kelvin (many thousands) The area of the sun multiplies by the gradient of the relationship between area and termperate for its class
    elif 0.0000003 < t_val <= 0.0013003:
        star.starClass = 'B'
        star.mass = random.uniform(21000 * (10**26), 160000 * (10**26))  # Units: kg
        star.radius = star.mass * 0.345323741007 + 1.47842  * 6.975 * (10**5)  # Units: kg
        star.temperature = math.floor(4*math.pi*star.radius*star.radius * 39.4729521557 + 8392.86)
    elif 0.0013003 < t_val <= 0.0073003:
        star.starClass = 'A'
        star.mass = random.uniform(14000 * (10**26), 21000 * (10**26))  # Units KG
        star.radius = star.mass * 0.571428571429 + 0.6  * 6.975 * (10**5)  # Units: kg
        star.temperature = math.floor(4*math.pi*star.radius*star.radius * 155.424749113 + 3671.88)
    elif 0.0073003 < t_val <= 0.0373003:
        star.starClass = 'F'
        star.mass = random.uniform(10400 * (10**26), 14000 * (10**26))  # Units: kg
        star.radius = star.mass * 0.694444444444 + 1.58333  * 6.975 * (10**5)  # Units: kg
        star.temperature = math.floor(4*math.pi*star.radius*star.radius * 187.24110952 + 2888.24)
    elif 0.0373003 < t_val <= 0.1133:
        star.starClass = 'G'
        star.mass = random.uniform(8000 * (10**26), 10400 * (10**26))  # Units Kg
        star.radius = star.mass * 0.791666666667 + 0.326667  * 6.975 * (10**5)  # Units: kg
        star.temperature = math.floor(4*math.pi*star.radius*star.radius * 158.797648383 + 3360.94)
    elif 0.1133 < t_val <= 0.2343:
        star.starClass = 'K'
        star.mass = random.uniform(4500 * (10**26), 8000 * (10**26))  # Units: kg
        star.radius = star.mass * 1.34615384615 + 0.365714 * 6.975 * (10**5)  # Units: kg
        star.temperature = math.floor(4*math.pi*star.radius*star.radius * 276.56674541 + 1997.03)
    else:
        star.starClass = 'M'
        star.mass = random.uniform(800 * (10**26), 4500 * (10**26))  # Units: kg
        star.radius = star.mass * 1.75675675676 + -0.77973 * 6.975 * (10**5)  # Units: kg
        star.temperature = math.floor(4*math.pi*star.radius*star.radius * 212.206590789 + 2393.33)

    orbit = Orbit()
    orbit.a = 0
    orbit.b = 0
    orbit.p = 0
    orbit.exentricity = 0
    orbit.bigM = 0
    orbit.rotation = 0
    orbit.period = 0
    orbit.save()

    star.orbit = orbit

    star.save()

    return star

def planetGen(name, seed, bigM, ismoon=False):

    planet = Planet(name=name, seed=seed)

    random.seed = planet.seed

    planet.axis = random.randint(0, 10)  # Planets inclination relative to the orbital plane # deg
    planet.tilt = random.uniform(0, 90)  # Planet's axis tilt in degrees from vertical # deg

    if ismoon:
        # idk about moon stuff
        t_val = random.random()

        if t_val <= 0.5:
            planet.type = 'rock'
            planet.mass = bigM * random.random() # Our solarsystem data Units: kg
            planet.radius = 5.4 * (10**-16)* (planet.mass**0.441)  # baised on exoplanet data extrapolation Units: AU


            # orbit shit
            orbit = Orbit()
            orbit.a = random.uniform(0.052995525, 0.231969) # baised on 1, 3ed quartiles of the exoplanet data Units: AU
            orbit.exentricity = random.uniform(0, 0.042) # baised on 1, 3ed quartiles of the exoplanet data
            orbit.b = math.sqrt((orbit.a**2) - (orbit.a**2) * (orbit.exentricity**2)) # using a derived vertion of this formular e == Sqrt[1 - b^2/a^2] Units: AU
            orbit.p = (orbit.b**2) / orbit.a # using this formular p=\frac{b^{2}}{a}
            orbit.bigM = bigM # mass of the centrial body Units: kg
            orbit.rotation = random.uniform(0, 360) # the rotation aroung the plane Units: deg
            orbit.period = 2*math.pi* math.sqrt(((orbit.a * 149597900000) ** 3) / (orbit.bigM * 6.674 * (10**-11))) # the period of orbit baised on Units: s (seconds)
            orbit.save()

            planet.orbit = orbit

        else:
            planet.type = 'ice'
            planet.mass = bigM * random.random() # Exoplanet data Units: kg
            planet.radius = 5.4 * (10**-16)* (planet.mass**0.441)  # baised on exoplanet data extrapolation Units: AU


            # orbit shit
            orbit = Orbit()
            orbit.a = random.uniform(0.052995525, 0.231969) # baised on 1, 3ed quartiles of the exoplanet data Units: AU
            orbit.exentricity = random.uniform(0, 0.042) # baised on 1, 3ed quartiles of the exoplanet data
            orbit.b = math.sqrt((orbit.a**2) - (orbit.a**2) * (orbit.exentricity**2)) # using a derived vertion of this formular e == Sqrt[1 - b^2/a^2] Units: AU
            orbit.p = (orbit.b**2) / orbit.a # using this formular p=\frac{b^{2}}{a}
            orbit.bigM = bigM # mass of the centrial body Units: kg
            orbit.rotation = random.uniform(0, 360) # the rotation aroung the plane Units: deg
            orbit.period = 2*math.pi* math.sqrt(((orbit.a * 149597900000) ** 3) / (orbit.bigM * 6.674 * (10**-11))) # the period of orbit baised on Units: s (seconds)
            orbit.save()

            planet.orbit = orbit


    else:
        t_val = random.random()

        if t_val <= 0.3:
            planet.type = 'gas'
            planet.mass = random.uniform(2.35938*(10**25), 6.86655*(10**26)) # Exoplanet data Units: kg
            planet.radius = 5.4 * (10**-16)* (planet.mass**0.441) # baised on exoplanet data extrapolation Units: AU

            # orbit shit
            orbit = Orbit()
            orbit.a = random.uniform(0.052995525, 0.231969) # baised on 1, 3ed quartiles of the exoplanet data Units: AU
            orbit.exentricity = random.uniform(0, 0.042) # baised on 1, 3ed quartiles of the exoplanet data
            orbit.b = math.sqrt((orbit.a**2) - (orbit.a**2) * (orbit.exentricity**2)) # using a derived vertion of this formular e == Sqrt[1 - b^2/a^2] Units: AU
            orbit.p = (orbit.b**2) / orbit.a # using this formular p=\frac{b^{2}}{a}
            orbit.bigM = bigM # mass of the centrial body Units: kg
            orbit.rotation = random.uniform(0, 360) # the rotation aroung the plane Units: deg
            orbit.period = 2*math.pi* math.sqrt(((orbit.a * 149597900000) ** 3) / (orbit.bigM * 6.674 * (10**-11))) # the period of orbit baised on Units: s (seconds)
            orbit.save()

            planet.orbit = orbit

        elif 0.3 < t_val <= 0.7:
            planet.type = 'rock'
            planet.mass = random.uniform(3.301*(10**23), 5.972*(10**24)) # Our solarsystem data Units: kg
            planet.radius = 5.4 * (10**-16)* (planet.mass**0.441)  # baised on exoplanet data extrapolation Units: AU


            # orbit shit
            orbit = Orbit()
            orbit.a = random.uniform(0.052995525, 0.231969) # baised on 1, 3ed quartiles of the exoplanet data Units: AU
            orbit.exentricity = random.uniform(0, 0.042) # baised on 1, 3ed quartiles of the exoplanet data
            orbit.b = math.sqrt((orbit.a**2) - (orbit.a**2) * (orbit.exentricity**2)) # using a derived vertion of this formular e == Sqrt[1 - b^2/a^2] Units: AU
            orbit.p = (orbit.b**2) / orbit.a # using this formular p=\frac{b^{2}}{a}
            orbit.bigM = bigM # mass of the centrial body Units: kg
            orbit.rotation = random.uniform(0, 360) # the rotation aroung the plane Units: deg
            orbit.period = 2*math.pi* math.sqrt(((orbit.a * 149597900000) ** 3) / (orbit.bigM * 6.674 * (10**-11))) # the period of orbit baised on Units: s (seconds)
            orbit.save()

            planet.orbit = orbit

        else:
            planet.type = 'ice'
            planet.mass = random.uniform(8.682*(10**25), 1.024*(10**26)) # Exoplanet data Units: kg
            planet.radius = 5.4 * (10**-16)* (planet.mass**0.441)  # baised on exoplanet data extrapolation Units: AU


            # orbit shit
            orbit = Orbit()
            orbit.a = random.uniform(0.052995525, 0.231969) # baised on 1, 3ed quartiles of the exoplanet data Units: AU
            orbit.exentricity = random.uniform(0, 0.042) # baised on 1, 3ed quartiles of the exoplanet data
            orbit.b = math.sqrt((orbit.a**2) - (orbit.a**2) * (orbit.exentricity**2)) # using a derived vertion of this formular e == Sqrt[1 - b^2/a^2] Units: AU
            orbit.p = (orbit.b**2) / orbit.a # using this formular p=\frac{b^{2}}{a}
            orbit.bigM = bigM # mass of the centrial body Units: kg
            orbit.rotation = random.uniform(0, 360) # the rotation aroung the plane Units: deg
            orbit.period = 2*math.pi* math.sqrt(((orbit.a * 149597900000) ** 3) / (orbit.bigM * 6.674 * (10**-11))) # the period of orbit baised on Units: s (seconds)
            orbit.save()

            planet.orbit = orbit


    #atmoshpere stuff
    atmosphere = Atmosphere()
    atmosphere.presure = 0 # presure of the atmosphere Units: KPa
    # all the rest are in percentages
    atmosphere.nitrogen = 0
    atmosphere.oxygen = 0
    atmosphere.argon = 0
    atmosphere.carbonDioxide = 0
    atmosphere.neon = 0
    atmosphere.helium = 0
    atmosphere.methane = 0
    atmosphere.sulpherDioxide = 0
    atmosphere.hydrogen = 0
    atmosphere.sodium = 0
    atmosphere.potasium = 0
    atmosphere.save()

    planet.atmosphere = atmosphere
    planet.gravity = ((6.67*10**-11) * planet.mass)/ (planet.radius * 149597900000)**2  # Gravitational pull at planetRadius

    planet.save()

    if ismoon == False:
        for i in range(0, random.randint(0,50)):
            planet.moons.add(planetGen(name=name+'moon'+str(i), seed=str(random.random()), bigM=bigM, ismoon=True))

    planet.save()

    return planet
