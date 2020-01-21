# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:43:40 2018

@author: coolertin100
"""

import requests
import json
import base64

"""
Get Access Token
"""

# specify the client and secret ids (from your app on the Spotify dashboard)
client = "5c0f29ba5f3d4c22881bc6d15800226d"
secret = "500ef7532d124f2993e615e42764b280"


baseUrl = "https://api.spotify.com/v1/me/"
# create a byte64 encoded version in the right format
auth = client + ":" + secret   # normal string
auth = bytes(auth, 'utf-8')    # convert to bytes (needed for next step)
auth64 = base64.b64encode(auth) # encode the string
auth64 = auth64.decode('utf-8') # convert back to a standard string

# set headers and data of the post
headers = {'Authorization': "Basic " + auth64 , 'Scopes': 'user-library-read' + ' playlist-read-private'}
data = {"grant_type":"client_credentials"}

# submit the request
url = "https://accounts.spotify.com/api/token"
r = requests.post(url, headers = headers, data = data)

#r = requests.get("https://accounts.spotify.com/authorize?client_id=5c0f29ba5f3d4c22881bc6d15800226d&response_type=code&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback")
resp = r.content.decode('utf-8')
#username = "coolertin100"
#token = AQAZ0SIWAIXuZyO62evRJD


url2 = 'https://accounts.spotify.com/authorize?client_id=' + client + '&response_type=code&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback&scope=user-read-private%20user-read-email%20user-read-library&state=34fFs29kd09'
r2 = requests.get(url2)
print(r2)
tokenString = json.loads(resp)
token = tokenString['access_token']
testurl = "https://api.spotify.com/v1/users/coolertin100/playlists"
testurl2 = "https://api.spotify.com/v1/me/tracks"

headers = {'Authorization': 'Bearer ' + token}

r1 = requests.get(testurl, headers = headers)
r2 = requests.get(testurl2, headers = headers)
#Unsure if I need to decode, but I don't think it can hurt

results = r1.json()
results2 = r2.json()
#test2 = results.content.decode('utf-8')
#print(results)

#print(results2)
newVar = results['items'][0]['href']

#print(newVar)
#print(results2)
newurl = "https://api.spotify.com/v1/me/playlists"

#playList = requests.get(newurl, headers = headers)
#playLists = []
#for i in playList['spotify']:
#    playLists.append(i)


#for j in playLists:
 #   playUrl = baseUrl + "playlists/" + j + "/tracks/"
  #  request = requests.get(playUrl, headers = headers)
