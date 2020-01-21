#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################
# In Python, use json module to convert JSON objects to 
# Python dictionaries
#Brendan Blais
################################################################

import requests
import json

# use requests.get to submit a 'get' request
link = "http://www.omdbapi.com/?apikey=1a04f0e1&s="

print("Enter Movie: ")
movieAppend = input()
link += movieAppend
page = requests.get(link)
print(link)


if page.status_code != requests.codes.ok :
    print("Request was not successful, status code:", page.status_code)
    print("Hit enter to continue...")
    input()
    exit()
    

# look at page content (as a string)
page.content


record = json.loads(page.content)


Movies = []
Ratings = []
for r in record['Search'] :
    Movies.append(r['Title'])
    Ratings.append(r["imdbID"])
for z in Movies:
    print(z)
count = 1
print("")
print("Enter the number corresponding to the desired movie:")
print("")
print("")
for i in Movies:
    print(f'[{count}] : {i}')
    count = count + 1
selector = int(input())
selector = selector -1
choice = Movies[selector]
link2 = "http://www.omdbapi.com/?apikey=1a04f0e1&i="
link2 += Ratings[selector]
#for y in Ratings:
#    print(y)
page2 = requests.get(link2)

if page2.status_code != requests.codes.ok :
    print("Request was not successful, status code:", page.status_code)
    print("Hit enter to continue...")
    input()
    exit()

info = json.loads(page2.content)


print("")
print("")
print(info['Title'])
print("Rated: " + info['Rated'])
print("Release Date: " + info['Released'])
print("Ratings: ")


otherRatings = info['Ratings']
for q in otherRatings :
    print("\t" + q['Source'] + ": " + q['Value'])

