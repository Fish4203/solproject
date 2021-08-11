# COLUMN pl_name:        Planet Name
# COLUMN hostname:       Host Name
# COLUMN default_flag:   Default Parameter Set
# COLUMN sy_snum:        Number of Stars
# COLUMN sy_pnum:        Number of Planets
# COLUMN sy_mnum:        Number of Moons
# COLUMN pl_refname:     Planetary Parameter Reference
# COLUMN pl_orbper:      Orbital Period [days] 7
# COLUMN pl_orbsmax:     Orbit Semi-Major Axis [au]) 8
# COLUMN pl_rade:        Planet Radius [Earth Radius] 9
# COLUMN pl_radj:        Planet Radius [Jupiter Radius] 10
# COLUMN pl_masse:       Planet Mass [Earth Mass] 11
# COLUMN pl_massj:       Planet Mass [Jupiter Mass] 12
# COLUMN pl_msinie:      Planet Mass*sin(i) [Earth Mas s] 13
# COLUMN pl_msinij:      Planet Mass*sin(i) [Jupiter Mass] 14
# COLUMN pl_cmasse:      Planet Mass*sin(i)/sin(i) [Earth Mass] 15
# COLUMN pl_cmassj:      Planet Mass*sin(i)/sin(i) [Jupiter Mass] 16
# COLUMN pl_bmasse:      Planet Mass or Mass*sin(i) [Earth Mass] 17
# COLUMN pl_bmassj:      Planet Mass or Mass*sin(i) [Jupiter Mass] 18
# COLUMN pl_dens:        Planet Density [g/cm**3] 19
# COLUMN pl_orbeccen:    Eccentricity
# COLUMN pl_insol:       Insolation Flux [Earth Flux]
# COLUMN pl_eqt:         Equilibrium Temperature [K]
# COLUMN pl_orbincl:     Inclination [deg]
# COLUMN ttv_flag:       Data show Transit Timing Variations
# COLUMN pl_ratdor:      Ratio of Semi-Major Axis to Stellar Radius
# COLUMN st_refname:     Stellar Parameter Reference
# COLUMN st_spectype:    Spectral Type
# COLUMN st_teff:        Stellar Effective Temperature [K]
# COLUMN st_rad:         Stellar Radius [Solar Radius]
# COLUMN st_mass:        Stellar Mass [Solar mass]
# COLUMN st_met:         Stellar Metallicity [dex]
# COLUMN st_metratio:    Stellar Metallicity Ratio
# COLUMN st_lum:         Stellar Luminosity [log(Solar)]
# COLUMN st_logg:        Stellar Surface Gravity [log10(cm/s**2)]
# COLUMN pl_nespec:      Number of Emission Spectroscopy Measurements
#

# key: pname, sname, default, nstar, nplanets, nmoons, orbitalp, orbitSemiM, Radius, mass, density, ecentricity, insolar flux, eq temp, inclnation
import time
import csv

def avg(list):
    li = []
    for i in list:
        if i != '':
            li.append(i)

    temp = 0
    for i in li:
        temp += float(i)

    try:
        temp = temp / len(li)
        return temp
    except:
        return 0

# open the file in the write mode
with open('tera.csv', 'r') as f:
    # create the csv writer
    plantemp = csv.reader(f)

    plan = []
    for j in plantemp:
        #print(j)
        plan.append(j)

    plan = plan[0]
print(plan)
with open('PS_2021.08.10_18.55.44.csv', 'r') as file:
    # create the csv writer
    plandata = csv.reader(file)

    planout = {}
    for i in plandata:
        #print(str(i[0]).upper())
        if i[0] in plan:
            #print(i)
            if i[0] in planout.keys():
                planout[i[0]][6].append(i[7])
                planout[i[0]][7].append(i[8])
                try:
                    planout[i[0]][8].extend([i[9], float(i[10])/ 11.2089])
                except:
                    planout[i[0]][8].extend([i[9], ''])

                try:
                    planout[i[0]][9].extend([i[11], i[13], i[15], i[17], float(i[12])/ 317.8, float(i[14])/ 317.8, float(i[16])/ 317.8, float(i[18])/ 317.8])
                except:
                    planout[i[0]][9].extend([i[11], i[13], i[15], i[17], '', '', '', ''])

                planout[i[0]][10].extend([i[19]])
                planout[i[0]][11].extend([i[20]])
                planout[i[0]][12].extend([i[21]])
                planout[i[0]][13].extend([i[22]])
                planout[i[0]][14].extend([i[23]])
            else:
                planout[i[0]] = i[:6]
                #print(len(planout[i[0]]), '1')
                planout[i[0]].append([i[7]])
                planout[i[0]].append([i[8]])
                try:
                    planout[i[0]].append([i[9], float(i[10])/ 11.2089])
                except:
                    planout[i[0]].append([i[9], ''])

                try:
                    planout[i[0]].append([i[11], i[13], i[15], i[17], float(i[12])/ 317.8, float(i[14])/ 317.8, float(i[16])/ 317.8, float(i[18])/ 317.8])
                except:
                    planout[i[0]].append([i[11], i[13], i[15], i[17], '', '', '', ''])
                #print(len(planout[i[0]]), '1.5')
                planout[i[0]].append([i[19]])
                planout[i[0]].append([i[20]])
                planout[i[0]].append([i[21]])
                planout[i[0]].append([i[22]])
                planout[i[0]].append([i[23]])
                #print(len(planout[i[0]]), '2')

for key in planout:
    for i in range(len(planout[key])):

        if type(planout[key][i]) == type([]):
            planout[key][i] = avg(planout[key][i])
            #print(planout[key][i])

# print(planout.keys(), len(planout))
# print(plan, len(plan))
# #print(planout['Kepler-1566 b'])
# print(planout, len(planout))
#
with open('neptdata.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    for key, i in planout.items():
        writer.writerow(i)
