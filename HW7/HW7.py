# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:45:54 2018

@author: coolertin100
"""

import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "blaisb@my.easternct.edu||CS Student"}
# use requests.get to submit a 'get' request
page = requests.get("https://gdancik.github.io/CSC-360/data/notes/schedule.html", headers=headers)

# check for valid status (https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)
page.status_code

if page.status_code != requests.codes.ok :
    print("Request was not successful, status code:", page.status_code)
    print("Hit enter to continue...")
    input()
    exit()

soup = BeautifulSoup(page.content, 'html.parser')

    
x = soup.title
y = x.string
z = y.split("for")
#print(z[1])
name = z[1]



times = soup.find_all("td")
columns = []
for i in times :
    columns.append(i.string)
newList = []
j = 2
while(j <len(columns)) :
    
    newList.append(columns[j])
    j = j + 3
newerList = []
classes = len(newList)
for k in newList :
    newerList.append(int(k))
creditTotal = 0
for l in newerList :
    creditTotal = creditTotal + l


printStatement = f'{name} is teaching {classes} classes ({creditTotal} credit hours)'
print(printStatement)