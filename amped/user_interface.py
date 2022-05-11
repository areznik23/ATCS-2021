import requests as req
from auth import access_token
from Track import Track
from Movie import Movie
import pandas as pd
from pandas import json_normalize
import pickle
from movies import movies
from sklearn.preprocessing import StandardScaler

# Resource: https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/
model = pickle.load(open('final_model.sav', 'rb'))
movies = json_normalize(movies)
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

def get_user_input():
    pref = input("Would you like to enter a song(0) or a playlist(1)? ")
    return pref

def get_track_title_input():
    title = input("Please enter a song title: ")
    return title.replace(' ', '+')

def get_playlist_title_input():
    title = input("Please enter a playlist title: ")
    return title.replace(' ', '+')

def get_track_data(title):
    r = req.get('https://api.spotify.com/v1/search?q='+title+'&type=track&limit=1', headers=headers)
    song_id = r.json()['tracks']['items'][0]['id']
    r = req.get('https://api.spotify.com/v1/audio-features/' + song_id, headers=headers)
    return song_id, r.json()

def get_playlist_data(title):
    r = req.get('https://api.spotify.com/v1/search?q=' + title + '&type=playlist&limit=1', headers=headers)
    playlist_id = r.json()['playlists']['items'][0]['id']
    r = req.get('https://api.spotify.com/v1/playlists/' + playlist_id, headers=headers)
    r = r.json()
    # treat the playlist as though it is a movie, create a movie object for the playlist
    mov = Movie('New', playlist_id)
    for track in r['tracks']['items']:
        song_id = track['track']['id']
        r = req.get('https://api.spotify.com/v1/audio-features/' + song_id, headers=headers)
        r = r.json()
        track = create_track(song_id, r)
        mov.add_track(track)
    mov.set_median_audio_features()
    result = mov.model_format()
    return playlist_id, result

def create_track(song_id, r):
    return Track(
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


def set_data(result, title):
    # Resource: https://stackoverflow.com/questions/21104592/json-to-pandas-dataframe
    data = json_normalize(result['audio_features'])
    data.insert(0, "title", title, False)
    # Resource: https://pandas.pydata.org/docs/user_guide/merging.html
    frames = [movies, data]
    # Resource: https://dataindependent.com/pandas/pandas-append-pd-dataframe-append/
    data = pd.concat(frames, ignore_index=True)
    return data

def scale_data(data):
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
    data = [data[len(data) - 1]]
    return data

def prediction(data):
    pred = model.predict(data)
    centroids = model.cluster_centers_
    labels = model.labels_
    return pred, centroids, labels

def get_recommendations(labels, pred):
    # Resource: https://stackoverflow.com/questions/16729574/how-to-get-a-value-from-a-cell-of-a-dataframe
    index = 0
    recs = []
    for label in labels[:len(labels)]:
        if pred == label:
            recs.append(movies.iloc[index]['title'])
        index += 1
    return recs

def output_recommendations(recs):
    print("\nYour Movie Recommendations\n")
    i = 1
    for movie in recs:
        print(i, "-", movie)
        i += 1
    print()

def main():
    pref = get_user_input()
    r = {}
    title = ''
    if pref == '0':
        title = get_track_title_input()
        song_id, r = get_track_data(title)
        track = create_track(song_id, r)
        r = track.format()
    if pref == '1':
        title = get_playlist_title_input()
        playlist_id, r = get_playlist_data(title)
    data = set_data(r, title)
    data = scale_data(data)
    pred, centroids, labels = prediction(data)
    recs = get_recommendations(labels, pred)
    output_recommendations(recs)

main()