'''
    Get list of the top 10,000 or so movies
    Movie Lens Database to retrieve the information
    Write a CSV file of all of those movies
    Loop through the movies to pull the soundtrack playlists
    Write the songs in the playlists to the CSV file
    Loop through the songs for each movie and feed them into the spotify API
    Get the features for each songs and write to the CSV file
'''

'Reference Source: https://stmorse.github.io/journal/spotify-api.html'

import requests as req

'Authentication Keys'
CLIENT_ID = '93edc838830a416b9c5fefb30a1d2eb1'
CLIENT_SECRET = '37bf5193927d41508307fe4e9b21b107'

'Function to receive access token'
def retrieve_acess_token():
    auth = req.post('https://accounts.spotify.com/api/token', {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    })

    access_token = auth.json()['access_token']

'stored value of access_token for export to other files'
access_token = 'BQCuT5_FYdWbrMxIaTV7AIxZs4TWpZF4iSMrCLa9FwjksNISeFvdj2iRP8BK5tvhXMr4woRb0RebCRauOYI'