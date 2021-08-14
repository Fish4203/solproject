import time
import csv
from matplotlib import pyplot
from numpy.random import normal
import numpy as np
import random
from scipy import stats

# open the file in the write mode
with open('teradata.csv', 'r') as f:
    # create the csv writer
    data = csv.reader(f)


    orbitPli = []
    semiMajorli = []
    radiusli = []
    massli = []
    densityli = []
    ectli = []
    eqtempli = []
    incli = []

    for i in data:
        if float(i[6]) != 0.0:
            orbitPli.append(float(i[6]))
        if float(i[7]) != 0.0:
            semiMajorli.append(float(i[7]))
        if float(i[8]) != 0.0:
            radiusli.append(float(i[8]))
        if float(i[9]) != 0.0:
            massli.append(float(i[9]))
        if float(i[10]) != 0.0:
            densityli.append(float(i[10]))
        if float(i[11]) != 0.0:
            ectli.append(float(i[11]))
        if float(i[13]) != 0.0:
            eqtempli.append(float(i[13]))
        if float(i[14]) != 0.0:
            incli.append(float(i[14]))

print(orbitPli)

# god function


print('hi')



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

testli = []
for i in range(1000):
    testli.append(frechetDistribution(1.167824118638451, 13.792245492349796, -2.379739625421347))
#print(testli)

# displaying stuff
# np.random.wald(mass[0], mass[1], 1000)
pyplot.hist(testli, bins=500, density=True) # blue
pyplot.hist(orbitPli, bins=500, density=True) # orange
pyplot.show()





from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl
from wolframclient.language import wlexpr
session=WolframLanguageSession()

orbitP = session.evaluate(wl.FindDistribution(orbitPli))
semiMajor = session.evaluate(wl.FindDistribution(semiMajorli))
radius = session.evaluate(wl.FindDistribution(radiusli))
mass = session.evaluate(wl.FindDistribution(massli))
density = session.evaluate(wl.FindDistribution(densityli))
ect = session.evaluate(wl.FindDistribution(ectli))
eqtemp = session.evaluate(wl.FindDistribution(eqtempli))
inc = session.evaluate(wl.FindDistribution(incli))

session.terminate()

print('')
print('orbit', orbitP)
print('')
print('semiMajor', semiMajor)
print('')
print('radius', radius)
print('')
print('mass', mass)
print('')
print('density', density)
print('')
print('ect', ect)
print('')
print('eqtemp', eqtemp)
print('')
print('inc', inc)
