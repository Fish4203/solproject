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
