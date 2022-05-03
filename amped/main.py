import requests as req
import numpy as np
import pandas as pd
import urllib

# extract all the movie titles from the csv and then get the playlists with those titles in them
# extract all of the songs from the playlists for those movie titles
# generate a new csv document with all of the data, extract the titles

from auth import access_token
from retrieve_data import titles

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}
def get_request_function(title):
    return title.replace(' ', '+')

playlist_ids = []
filtered_titles = []
for title in titles:
    title = get_request_function(title)
    r = req.get('https://api.spotify.com/v1/search?q='+title+'&type=playlist&limit=50', headers=headers)
    try:
        id = r.json()['playlists']['items'][0]['id']
        playlist_ids.append(id)
        print(title)
        filtered_titles.append(title)
    except:
        continue


# Reference Source for this task: https://cmdlinetips.com/2018/01/how-to-create-pandas-dataframe-from-multiple-lists/
def output_data():
    d = {'titles': filtered_titles, 'playlist_id': playlist_ids}
    df = pd.DataFrame(d)
    print(df)
    df.to_csv('data.csv', index=False)

output_data()

# r = req.get('https://api.spotify.com/v1/search?q=Original+Motion+Picture+Soundtrack&type=playlist&limit=50', headers=headers)
# r = r.json()
# for item in r['playlists']['items']:
#     print(item['name'])
#
# new_id = r['playlists']['items'][1]['id']

# r = req.get('https://api.spotify.com/v1/playlists/' + new_id, headers=headers)
# r = r.json()
# print(r)
# for playlist in r:
#     print(playlist['name'])
