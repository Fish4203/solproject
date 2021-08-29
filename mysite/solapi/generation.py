from .models import *
import random
import math
import numpy as np
from scipy import stats


def mixtureDistribution(probli, distli):
    return np.random.choice(distli,p=probli)

def weibullDistribution(shape, scale, loc):
    temp = -1
    while temp < 0:
        temp = float(stats.weibull_min.rvs(shape, loc=loc, scale=scale, size=1))
    return temp

def logNormalDistribution(loc, stdev):
    temp = -1
    while temp < 0:
        temp = float(np.random.lognormal(loc, stdev, 1))
    return temp

def normalDistribution(loc, stdev):
    temp = -1
    while temp < 0:
        temp = float(np.random.normal(loc, stdev, 1))
    return temp

def cauchyDistribution(loc, scale):
    temp = -1
    while temp < 0:
        temp = float(stats.cauchy.rvs(loc=loc, scale=scale,  size=1))
    return temp

def studentTDistribution(loc, scale, free):
    temp = -1
    while temp < 0:
        temp = float(stats.nct.rvs(loc=loc, df=free, nc=0, scale=scale, size=1))
    return temp

def gammaDistribution(loc, stdev):
    temp = -1
    while temp < 0:
        temp = float(np.random.wald(loc, stdev, 1))
    return temp

def inverseGaussianDistribution(loc, stdev):
    temp = -1
    while temp < 0:
        temp = float(np.random.wald(loc, stdev, 1))
    return temp

def frechetDistribution(shape, scale, loc):
    temp = -1
    while temp < 0:
        temp = float(stats.invweibull.rvs(shape, loc=loc, scale=scale, size=1))
    return temp

def extremeValueDistribution(loc, scale):
    temp = -1
    while temp < 0:
        temp = float(stats.genextreme.rvs(0, loc=loc, scale=scale, size=1))
    return temp

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

    random.seed(system.seed)

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


def asteroidGen(name, seed):
    # idk what im doing
    ast = Asteroid(name=name, seed=seed)
    random.seed(ast.seed)

    orbit = Orbit()
    orbit.a = random.uniform(0.052995525, 0.231969) # baised on 1, 3ed quartiles of the exoplanet data Units: AU
    orbit.exentricity = random.uniform(0, 0.042) # baised on 1, 3ed quartiles of the exoplanet data
    orbit.b = math.sqrt((orbit.a**2) - (orbit.a**2) * (orbit.exentricity**2)) # using a derived vertion of this formular e == Sqrt[1 - b^2/a^2] Units: AU
    orbit.p = (orbit.b**2) / orbit.a # using this formular p=\frac{b^{2}}{a}
    orbit.bigM = bigM # mass of the centrial body Units: kg
    orbit.rotation = random.uniform(0, 360) # the rotation aroung the plane Units: deg
    orbit.period = 2*math.pi* math.sqrt(((orbit.a * 149597900000) ** 3) / (orbit.bigM * 6.674 * (10**-11))) # the period of orbit baised on Units: s (seconds)
    orbit.save()

    r = 0

    # types
    # C-type
    # distance: 2 - 3.5
    # makeup:
    # The S-types ("stony") are made up of silicate materials and nickel-iron.
    # The M-types are metallic (nickel-iron). The asteroids' compositional differences are related to how far from the Sun they formed. Some experienced high temperatures after they formed and partly melted, with iron sinking to the center and forcing basaltic (volcanic) lava to the surface.


def starGen(name, seed):
    # this should be mostly done and working for unery systems
    star = Star(name=name, seed=seed)
    random.seed(star.seed)

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

    random.seed(seed)
    np.random.seed(hash(seed))


    if ismoon:
        pass
        # im going to have to re do this

    else:
        t_val = random.random()

        if t_val <= 0.3:
            # i think this is done accurate data
            planet.type = 'gas'

            planet.axis = MixtureDistribution([0.0631400621068621, 0.936859937893138], [NormalDistribution(55.414243373649896, 47.580830239177686), NormalDistribution(87.20081252714141, 2.3894923435217335)])  # Planets inclination relative to the orbital plane # deg
            planet.tilt = random.uniform(0, 90)  # Planet's axis tilt in degrees from vertical Units: deg Sorce: idk

            planet.mass = inverseGaussianDistribution(928.824701947788, 300.0479022811526) # nasa data Units: kg
            planet.radius = studentTDistribution(6.930761956160252, 1.366846871550845, 2.6348570001976364) # nasa data Units: AU

            # orbit shit
            orbit = Orbit()
            orbit.a = mixtureDistribution([0.4704883266643796, 0.5295116733356204], [logisticDistribution(0.0705557404282793, 0.04076153656660551), logNormalDistribution(0.4999743569155569, 1.869202031165252)]) # baised on 1, 3ed quartiles of the exoplanet data Units: AU
            orbit.exentricity = MixtureDistribution([0.6770449886638618, 0.3229550113361382], [normalDistribution(0.10876155772380555, 0.0983128535740209), normalDistribution(0.40545065381711914, 0.21867684220052921)]) # baised on 1, 3ed quartiles of the exoplanet data
            orbit.b = math.sqrt((orbit.a**2) - (orbit.a**2) * (orbit.exentricity**2)) # using a derived vertion of this formular e == Sqrt[1 - b^2/a^2] Units: AU
            orbit.p = (orbit.b**2) / orbit.a # using this formular p=\frac{b^{2}}{a}
            orbit.bigM = bigM # mass of the centrial body Units: kg
            orbit.rotation = random.uniform(0, 360) # the rotation aroung the plane Units: deg
            orbit.period = 2*math.pi* math.sqrt(((orbit.a * 149597900000) ** 3) / (orbit.bigM * 6.674 * (10**-11))) # the period of orbit baised on Units: s (seconds)
            orbit.save()

            planet.orbit = orbit

        elif 0.3 < t_val <= 0.6:
            # good i think
            planet.type = 'super'

            planet.axis = mixtureDistribution([0.11731760749857346, 0.8826823925014264], [cauchyDistribution(83.72530831316405, 1.6610374331407494), normalDistribution(88.47424024919356, 1.1263648417013203)])  # Planets inclination relative to the orbital plane Units: deg
            planet.tilt = random.uniform(0, 90)  # Planet's axis tilt in degrees from vertical Units: deg Sorce: idk

            planet.mass = frechetDistribution(1.0410474390574176, 4.679796043693668, -0.21857637698892585) # nasa data Units: kg
            planet.radius = mixtureDistribution([0.6591604913899113, 0.3408395086100887], [logNormalDistribution(0.020374738630618384, 0.2852790839895245), cauchyDistribution(1.3255728404106326, 0.1905523566962049)]) # nasa data Units: AU

            # orbit shit
            orbit = Orbit()
            orbit.a = mixtureDistribution([0.38188724247370265, 0.6181127575262974], [normalDistribution(0.007755002403111972, 0.03899417827710038), logNormalDistribution(-1.9302655516861702, 0.7177081236362043)]) # baised on 1, 3ed quartiles of the exoplanet data Units: AU
            orbit.exentricity = weibullDistribution(2.055091374906744, 0.2356541343063726, -0.10782315849124682) # baised on 1, 3ed quartiles of the exoplanet data
            orbit.b = math.sqrt((orbit.a**2) - (orbit.a**2) * (orbit.exentricity**2)) # using a derived vertion of this formular e == Sqrt[1 - b^2/a^2] Units: AU
            orbit.p = (orbit.b**2) / orbit.a # using this formular p=\frac{b^{2}}{a}
            orbit.bigM = bigM # mass of the centrial body Units: kg
            orbit.rotation = random.uniform(0, 360) # the rotation aroung the plane Units: deg
            orbit.period = 2*math.pi* math.sqrt(((orbit.a * 149597900000) ** 3) / (orbit.bigM * 6.674 * (10**-11))) # the period of orbit baised on Units: s (seconds)
            orbit.save()

            planet.orbit = orbit

        elif 0.6 < t_val <= 0.9:
            # good i think
            planet.type = 'nept'

            planet.axis = mixtureDistribution([0.5222828598935413, 0.4777171401064587], [cauchyDistribution(88.41826474259561, 0.5906718096103573), normalDistribution(89.55737039572608, 0.31020863804072724)])  # Planets inclination relative to the orbital plane Units: deg
            planet.tilt = random.uniform(0, 90)  # Planet's axis tilt in degrees from vertical Units: deg Sorce: idk

            planet.mass = mixtureDistribution([0.4757270079315563, 0.5242729920684437], [normalDistribution(11.07917790736175, 4.536808439727342), logNormalDistribution(3.190815909191761, 1.3715705638998301)]) # nasa data Units: kg
            planet.radius = mixtureDistribution([0.5802285251266968, 0.41977147487330324], [normalDistribution(1.759518599763769, 0.31262774425245027), cauchyDistribution(2.4736624001248617, 0.3686254156495506)]) # nasa data Units: AU

            # orbit shit
            orbit = Orbit()
            orbit.a = mixtureDistribution([0.6860513516635095, 0.31394864833649055], [cauchyDistribution(0.19401727336333158, 0.07998092634483735), normalDistribution(0.043303343659861014, 0.03824274158482946)]) # baised on 1, 3ed quartiles of the exoplanet data Units: AU
            orbit.exentricity = extremeValueDistribution(0.06610828779106338, 0.09986244794438565) # baised on 1, 3ed quartiles of the exoplanet data
            orbit.b = math.sqrt((orbit.a**2) - (orbit.a**2) * (orbit.exentricity**2)) # using a derived vertion of this formular e == Sqrt[1 - b^2/a^2] Units: AU
            orbit.p = (orbit.b**2) / orbit.a # using this formular p=\frac{b^{2}}{a}
            orbit.bigM = bigM # mass of the centrial body Units: kg
            orbit.rotation = random.uniform(0, 360) # the rotation aroung the plane Units: deg
            orbit.period = 2*math.pi* math.sqrt(((orbit.a * 149597900000) ** 3) / (orbit.bigM * 6.674 * (10**-11))) # the period of orbit baised on Units: s (seconds)
            orbit.save()

            planet.orbit = orbit

        else:
            # good i think
            planet.type = 'tera'

            planet.axis = mixtureDistribution([0.0977459957793555, 0.9022540042206444], [normalDistribution(74.84281898022508, 11.62506209999429), normalDistribution(88.05388760287485, 1.569147970706866)])  # Planets inclination relative to the orbital plane Units: deg
            planet.tilt = random.uniform(0, 90)  # Planet's axis tilt in degrees from vertical Units: deg Sorce: idk

            planet.mass = weibullDistribution(0.49037496592107127, 4.413426662039768, 0.01749999999993345) # nasa data Units: kg
            planet.radius = studentTDistribution(0.6584412776941425, 0.10191541528132546, 1.2203071923546798) # nasa data Units: AU

            # orbit shit
            orbit = Orbit()
            orbit.a = logNormalDistribution(-3.122001182763973, 0.762901057268751) # baised on 1, 3ed quartiles of the exoplanet data Units: AU
            orbit.exentricity = weibullDistribution(0.6772026496221208, 0.05688620082154043) # baised on 1, 3ed quartiles of the exoplanet data
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
    atmosphere.save()

    planet.atmosphere = atmosphere
    planet.gravity = ((6.67*10**-11) * planet.mass)/ (planet.radius * 149597900000)**2  # Gravitational pull at planetRadius

    planet.save()

    # if ismoon == False:
    #     for i in range(0, random.randint(0,50)):
    #         planet.moons.add(planetGen(name=name+'moon'+str(i), seed=str(random.random()), bigM=planet.mass, ismoon=True))

    planet.save()

    return planet
