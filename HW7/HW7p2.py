# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 22:13:55 2018

@author: coolertin100
"""

import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "blaisb@my.easternct.edu||CS Student"}
# use requests.get to submit a 'get' request
page = requests.get("http://www.easternct.edu/computerscience/faculty/", headers=headers)
# check for valid status (https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)
page.status_code

if page.status_code != requests.codes.ok :
    print("Request was not successful, status code:", page.status_code)
    print("Hit enter to continue...")
    input()
    exit()

soup = BeautifulSoup(page.content, 'html.parser')
#"row-3 odd"
offices = soup.find_all("tr", {"class" : "row-3 odd"})
newList = []
for i in offices :
    newList.append(i.getText())
officesNew = []
for l in newList :
    officesNew.append(str(l))


profs = soup.find_all("tr", {"class" : "row-1 odd"})
newerList = []
for j in profs :
    newerList.append(j.getText())
newestList = []
for k in newerList :
    newestList.append(str(k))

    

print(f'{"Name":40}\t{"Offices":30}')
z = 0
while(z<len(newestList)) :
    print(f'{newestList[z]:40}\t{officesNew[z]:30}')
    z = z + 1
#"row-3 odd"