# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 12:28:33 2018

@author: coolertin100
"""

import requests
import time
from bs4 import BeautifulSoup
import pandas as pd

headers = {"User-Agent": "blaisb@my.easternct.edu||CS Student"}
# use requests.get to submit a 'get' request
urls = [ "https://www.imdb.com/title/tt0109830/?ref_=fn_al_tt_1",
         "https://www.imdb.com/title/tt0076759/?ref_=fn_tt_tt_1",
         "https://www.imdb.com/title/tt0368226/?ref_=nv_sr_2",
         "https://www.imdb.com/title/tt0117705/",
         "https://www.imdb.com/title/tt2322441/?ref_=nv_sr_1"
         ]

titles = []
ratings = []
for i in urls :
    page = requests.get(i, headers = headers)
    if page.status_code != requests.codes.ok :
        print("Request was not successful, status code:", page.status_code)
        print("Hit enter to continue...")
        input()
        exit()
    temp = BeautifulSoup(page.content, 'html.parser')
    titleTemp = temp.find("h1").getText()
    titles.append(str(titleTemp))
    ratingTemp = temp.find("div", {"class" : "ratingValue"}).find("span").text
    ratings.append(str(ratingTemp))
    time.sleep(1)

newRatings = []
for j in ratings :
    otherTemp = float(j)
    newRatings.append(otherTemp)


fancyGraph = pd.DataFrame(data = {"Titles":titles, "Ratings":newRatings})

plt = fancyGraph.plot.bar(x = "Titles", y = "Ratings", 
            title = "IMDB Movie Ratings",
            legend = False, rot = 90)

plt.set_xlabel("Movie Title")
plt.set_ylabel("Ratings (Out of 10)")