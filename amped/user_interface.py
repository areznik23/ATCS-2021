import requests as req
from auth import access_token
from Track import Track
import pandas as pd
from pandas import json_normalize
import pickle
from movies import movies
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

#
# model = pickle.load(open('final_model.sav', 'rb'))
movies = json_normalize(movies)

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

title = input("Please enter a song title: ")
title.replace(' ', '+')
r = req.get('https://api.spotify.com/v1/search?q='+title+'&type=track&limit=1', headers=headers)
song_id = r.json()['tracks']['items'][0]['id']
r = req.get('https://api.spotify.com/v1/audio-features/' + song_id, headers=headers)
r = r.json()
track = Track(
    song_id,
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
data = json_normalize(track.format()['audio_features'])
data.insert(0, "title", title, False)
frames = [movies, data]
data = pd.concat(frames, ignore_index=True)

data = data[[
    'audio_features.danceability',
    'audio_features.energy',
    'audio_features.key',
    'audio_features.loudness',
    'audio_features.mode',
    'audio_features.speechiness',
    'audio_features.acousticness',
    'audio_features.instrumentalness',
    'audio_features.liveness',
    'audio_features.valence',
    'audio_features.tempo',
]]

scaler = StandardScaler().fit(data)
data = scaler.transform(data)

k = 8

model = KMeans(n_clusters=k).fit(data)
centroids = model.cluster_centers_
labels = model.labels_

pred = labels[len(labels) - 1]
index = 0
recs = []
for label in labels[:len(labels) - 1]:
    if pred == label:
        print(movies.loc[[index], 'title'])
    index += 1
print("\nYour Movie Recommendations\n")
print(recs)