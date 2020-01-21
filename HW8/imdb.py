# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 12:48:14 2018

@author: coolertin100
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()

driver = webdriver.Firefox(firefox_options=options)

driver.get("https://www.imdb.com/")
print(driver.title)

assert ("IMDb - Movies, TV and Celebrities - IMDb" in driver.title)
search = driver.find_element_by_id("navbar-query")
search.clear()

time.sleep(1)
search.send_keys("Deadpool")
time.sleep(2)
search.send_keys(Keys.RETURN)
time.sleep(4)

result = driver.find_element_by_class_name("result_text")
movie = result.find_element_by_tag_name("a")
movie.click()
time.sleep(1)


rating = driver.find_element_by_class_name("imdbRating")
realRating = rating.find_element_by_tag_name("span").text

name = driver.find_element_by_class_name("title_wrapper")
realName = name.find_element_by_tag_name("h1").text



print(f"{realName} has a rating of, {realRating}")

