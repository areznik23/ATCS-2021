"""
Amped Music/Movie Project

@author: Alex Reznik
@version: 10 May 2022
"""


# Note: Errors resulted in use of only <200 movies rather than intended 1000
# Note: Used JSON output to construct the movies.py array by copying and pasting output so as not to lose time be rerunning

import requests as req
import pandas as pd
from Movie import Movie
from Track import Track
from auth import access_token
from retrieve_data import titles
from pandas import json_normalize

# extract all the movie titles from the csv and then get the playlists with those titles in them
# extract all of the songs from the playlists for those movie titles
# generate a new csv document with all of the data, extract the titles

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# Formatting the request for the spotify api
def get_request_function(title):
    return title.replace(' ', '+')

# gets the id of the playlist for a given movie
def get_playlist_id():
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

data = pd.read_csv('data.csv')
entries = []
# key features to analyze over
# have to get the median audio features for each of the movies
# upload all of this data into a json file that will then be used to build the model
# development of the model and then interface with users
# method for the number of k means clusters: https://blog.cambridgespark.com/how-to-determine-the-optimal-number-of-clusters-for-k-means-clustering-14f27070048f

# index = 170 because was trying to get the movies after encountering errors and slow running
# intended to retrieve the songs for each playlist for each movie
def get_song_ids():
    i = 0
    titles = list(data['titles'])
    movies = []
    for playlist in data['playlist_id']:
        r = req.get('https://api.spotify.com/v1/playlists/' + playlist, headers=headers)
        r = r.json()
        mov = Movie(titles[i], playlist)
        try:
            for track in r['tracks']['items']:
                    id = track['track']['id']
                    r = req.get('https://api.spotify.com/v1/audio-features/' + id, headers=headers)
                    r = r.json()
                    track = Track(
                        id,
                        r['danceability'],
                        r['energy'],
                        r['key'],
                        r['loudness'],
                        r['mode'],
                        r['speechiness'],
                        r['acousticness'],
                        r['instrumentalness'],
                        r['liveness'],
                        r['valence'],
                        r['tempo']
                    )
                    mov.add_track(track)
        except TypeError or KeyError:
            continue
        mov.set_median_audio_features()
        movies.append(mov.format())
        print(mov.format())
        i += 1
    # reference source for this step: https://sparkbyexamples.com/pandas/pandas-convert-json-to-dataframe/
    df = json_normalize(movies)
    output_dataframe(df)

# outputs the dataframe of all of the songs
def output_dataframe(df):
    df.to_csv('movie_audio.csv', index=False)

get_song_ids()
