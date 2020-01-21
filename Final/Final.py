# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:17:38 2018

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

# create a byte64 encoded version in the right format
auth = client + ":" + secret   # normal string
auth = bytes(auth, 'utf-8')    # convert to bytes (needed for next step)
auth64 = base64.b64encode(auth) # encode the string
auth64 = auth64.decode('utf-8') # convert back to a standard string

# set headers and data of the post
headers = {'Authorization': "Basic " + auth64}
data = {"grant_type":"client_credentials"}

# submit the request
url = "https://accounts.spotify.com/api/token"
r = requests.post(url, headers = headers, data = data)

#r = requests.get("https://accounts.spotify.com/authorize?client_id=5c0f29ba5f3d4c22881bc6d15800226d&response_type=code&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback")
resp = r.content.decode('utf-8')
#username = "coolertin100"
#token = AQAZ0SIWAIXuZyO62evRJD


url2 = requests.get('https://accounts.spotify.com/authorize?client_id=' + client + '&response_type=code&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback&scope=user-read-private%20user-read-email&state=34fFs29kd09')

tokenString = json.loads(resp)
token = tokenString['access_token']
testurl = "	https://api.spotify.com/v1/me/player/recently-played"

headers = {'Authorization': 'Bearer ' + token}

r1 = requests.get(testurl, headers = headers)
#Unsure if I need to decode, but I don't think it can hurt

results = r1.json()
#test2 = results.content.decode('utf-8')
#for i in results:
    #print(results['external_urls'])
