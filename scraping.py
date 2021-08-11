from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import csv


driver = webdriver.Firefox()

driver.get('https://exoplanets.nasa.gov/discovery/exoplanet-catalog/')

drop = driver.find_element_by_xpath("//select[@name='per_page']")

# page length
#print(drop.find_elements_by_tag_name("option")[2].text)
drop.find_elements_by_tag_name("option")[2].click()

# gass select
gass = driver.find_element_by_name('planet_type-terrestrial')
gass.click()
#print(gass.text)

#print(drop.text)

plan = set()
for i in range(10):
    time.sleep(2)

    for ent in driver.find_elements_by_class_name('data_results')[0].find_elements_by_tag_name('a'):
        #print(ent.find_elements_by_tag_name('a')[0].text)
        plan.add(ent.text)

    # tree
    page = driver.find_elements_by_class_name('page_num')[0]
    #print(page.get_attribute('value'))

    #print(dir(page))

    page.clear()
    page.send_keys(str(i+1))

    #print(page.get_attribute('value'))


driver.close()

# open the file in the write mode
with open('tera.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(plan)


print(plan, len(plan))


# This file was produced by the NASA Exoplanet Archive  http://exoplanetarchive.ipac.caltech.edu
# Tue Aug 10 18:55:44 2021
#
# User preference: *
#
# CONSTRAINT:  order by pl_masse asc
#
# COLUMN pl_name:        Planet Name
# COLUMN hostname:       Host Name
# COLUMN default_flag:   Default Parameter Set
# COLUMN sy_snum:        Number of Stars
# COLUMN sy_pnum:        Number of Planets
# COLUMN sy_mnum:        Number of Moons
# COLUMN pl_refname:     Planetary Parameter Reference
# COLUMN pl_orbper:      Orbital Period [days]
# COLUMN pl_orbsmax:     Orbit Semi-Major Axis [au])
# COLUMN pl_rade:        Planet Radius [Earth Radius]
# COLUMN pl_radj:        Planet Radius [Jupiter Radius]
# COLUMN pl_masse:       Planet Mass [Earth Mass]
# COLUMN pl_massj:       Planet Mass [Jupiter Mass]
# COLUMN pl_msinie:      Planet Mass*sin(i) [Earth Mass]
# COLUMN pl_msinij:      Planet Mass*sin(i) [Jupiter Mass]
# COLUMN pl_cmasse:      Planet Mass*sin(i)/sin(i) [Earth Mass]
# COLUMN pl_cmassj:      Planet Mass*sin(i)/sin(i) [Jupiter Mass]
# COLUMN pl_bmasse:      Planet Mass or Mass*sin(i) [Earth Mass]
# COLUMN pl_bmassj:      Planet Mass or Mass*sin(i) [Jupiter Mass]
# COLUMN pl_bmassprov:   Planet Mass or Mass*sin(i) Provenance
# COLUMN pl_dens:        Planet Density [g/cm**3]
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
