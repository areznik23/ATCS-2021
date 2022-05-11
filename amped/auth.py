'''
    Initial Project Pseudocode

    Get list of the top 10,000 or so movies
    Movie Lens Database to retrieve the information
    Write a CSV file of all of those movies
    Loop through the movies to pull the soundtrack playlists
    Write the songs in the playlists to the CSV file
    Loop through the songs for each movie and feed them into the spotify API
    Get the features for each songs and write to the CSV file
'''

# Resource: https://developer.spotify.com/documentation/web-api/reference/#/
# Resource: https://stmorse.github.io/journal/spotify-api.html

import requests as req

# Authentication Keys for the program
CLIENT_ID = '93edc838830a416b9c5fefb30a1d2eb1'
CLIENT_SECRET = '37bf5193927d41508307fe4e9b21b107'

# Retrieves the access token from the spotify API
def retrieve_acess_token():
    auth = req.post('https://accounts.spotify.com/api/token', {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    })

    return auth.json()['access_token']

# Stored value of access_token for export to other files
access_token = retrieve_acess_token()

