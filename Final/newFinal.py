# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 14:39:49 2018

@author: coolertin100
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

# on your own machine

options = Options()
options.headless = True

driver = webdriver.Firefox()

driver.get('https://www.wunderground.com/history/')


#size = input("Please enter whether you want to look at State, City, National, or Global weather data")
#Gets user input of the desired day, month, year and location. 
location = input("Please enter desired Zip Code:")
#year = input("Please enter the year in which you wish to start the search")

#month = input("Please enter month")
time.sleep(5)
#location = "06351"
year = 2015

size = "State"
summer = "ju"
spring = "ma"
fall = "se"
winter = "de"
stryear = str(year)

#Handles the dropdowns and searchbar





statedrop = driver.find_element_by_class_name("year")
statedrop.send_keys(year)
time.sleep(.5)
monthdrop = driver.find_element_by_id("histSearch")
monthdrop.send_keys(location)

time.sleep(.5)
byeardrop = driver.find_element_by_class_name("month")
byeardrop.send_keys(spring)
time.sleep(.5)

eyeardrop = driver.find_element_by_class_name("day")
eyeardrop.send_keys("21")

statedrop = driver.find_element_by_class_name("year")
statedrop.send_keys(year)
time.sleep(1)
statedrop = driver.find_element_by_class_name("year")
statedrop.send_keys(year)


eyeardrop = driver.find_element_by_class_name("day")
eyeardrop.send_keys("21")

statedrop = driver.find_element_by_class_name("year")
statedrop.send_keys(year)

statedrop.send_keys(year)

time.sleep(1)
inputbutton = driver.find_element_by_xpath('//*[@id="trip"]/input[5]')
inputbutton.send_keys(Keys.RETURN)


time.sleep(25)
avgTemps = []
wind = driver.find_element_by_xpath('//*[@id="inner-content"]/div[2]/div[2]/div/div[1]/div/div/city-history-summary/div/div[2]/table/tbody[5]/tr[1]/td[1]').text
temp = driver.find_element_by_xpath('//*[@id="inner-content"]/div[2]/div[2]/div/div[1]/div/div/city-history-summary/div/div[2]/table/tbody[1]/tr[3]/td[1]').text
#time.sleep(5)
print(temp)
temp = int(temp)
avgTemps.append(temp)
years = []
rains = []
winds = []
winds.append(wind)
years.append(year)
d = driver.find_element_by_class_name("selector")
d2 = d.find_elements_by_tag_name("div")
d2[2].click()
time.sleep(10)
rain = driver.find_element_by_xpath('//*[@id="inner-content"]/div[2]/div[2]/div/div[1]/div/div/city-history-summary/div/div[2]/table/tbody[2]/tr/td[2]').text
rain = float(rain)
rains.append(rain)

counter = 0
tempYear = year - 5
while counter < 4:
    try:
        
        print('Entering Loop')
        newdriver = webdriver.Firefox(options=options)
        
        newdriver.get('https://www.wunderground.com/history/')
        time.sleep(1)
        
        
        
        time.sleep(25)
        
        monthdrop = newdriver.find_element_by_id("histSearch")
        monthdrop.send_keys(location)
        
        
        byeardrop = newdriver.find_element_by_class_name("month")
        byeardrop.send_keys(spring)
        
        eyeardrop = newdriver.find_element_by_class_name("day")
        eyeardrop.send_keys("21")
        
        statedrop = newdriver.find_element_by_class_name("year")
        
        statedrop.send_keys(tempYear)
        
        statedrop.send_keys(tempYear)
        
        inputbutton = newdriver.find_element_by_xpath('//*[@id="trip"]/input[5]')
        inputbutton.send_keys(Keys.RETURN)
        
        time.sleep(15)
        
        temp = newdriver.find_element_by_xpath('//*[@id="inner-content"]/div[2]/div[2]/div/div[1]/div/div/city-history-summary/div/div[2]/table/tbody[1]/tr[3]/td[1]').text
        print(temp)
        wind = newdriver.find_element_by_xpath('//*[@id="inner-content"]/div[2]/div[2]/div/div[1]/div/div/city-history-summary/div/div[2]/table/tbody[5]/tr[1]/td[1]').text
        temp = int(temp)
        wind = int(wind)
        avgTemps.append(temp)
        winds.append(wind)
        years.append(tempYear)
        
        d = newdriver.find_element_by_class_name("selector")
        d2 = d.find_elements_by_tag_name("div")
        d2[2].click()
        time.sleep(10)
        
        rain = newdriver.find_element_by_xpath('//*[@id="inner-content"]/div[2]/div[2]/div/div[1]/div/div/city-history-summary/div/div[2]/table/tbody[2]/tr/td[2]').text
        rain = float(rain)
        rains.append(rain)
        
        tempYear = tempYear - 5
        counter = counter + 1
    except NoSuchElementException:
#       print('At counter ' + counter + 'there was no data, adding a 0 to the list to show exception')
        print('error')
        counter = counter + 1
        avgTemps.append(0)
        winds.append(0)
        years.append(tempYear)
        rains.append(0)
        tempYear = tempYear - 5

rains.append(0)
    

df= pd.DataFrame(data = {"Years":years, "avg_temp":avgTemps})

fd = pd.DataFrame(data = {"Years":years, "hi_wind":winds})

rando = pd.DataFrame(data ={"Years":years, "avg_rain":rains})

//*[@id="inner-content"]/div[2]/div[2]/div/div[1]/div/div/city-history-summary/div/div[2]/table/tbody[2]/tr/td[2]

plt = df.plot.bar(x = "Years", y = "avg_temp", 
            title = "Avg Temps, past 25 years",
            legend = False, rot = 0)

plt.set_xlabel("Years")
plt.set_ylabel("Temperature (Degrees Fahrenheit)")


plt = fd.plot.bar(x = "Years", y = "hi_wind", 
            title = "High Winds, past 25 years",
            legend = False, rot = 0)

plt.set_xlabel("Years")
plt.set_ylabel("Winds in MpH")


plt = rando.plot.bar(x = "Years", y = "avg_rain", 
            title = "Avg Rain, past 20 years",
            legend = False, rot = 0)

plt.set_xlabel("Years")
plt.set_ylabel("Rain Avg")
#print(driver.find_element_by_xpath("//tr//td[2]//table[1]").getText())
headers = {"User-Agent": "blaisb@my.easternct.edu || CS Student working on final project"}

# use requests.get to submit a 'get' request, and specify header
page = requests.get(dayurl, 
                    headers=headers)

if page.status_code != requests.codes.ok :
    print("Request was not successful, status code:", page.status_code)
    exit()
    
# Parse page using BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find_all("div", {"class":"region-content-summary"})
for i in table:
    print(i.prettify())

