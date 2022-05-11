from movies import movies
from pandas import json_normalize
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pickle

movies = json_normalize(movies)

x = movies[[
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

scaler = StandardScaler().fit(x)
x = scaler.transform(x)

# inertias = []
# for k in range(1, 20):
#     kmeanModel = KMeans(n_clusters=k).fit(x)
#     inertias.append(kmeanModel.inertia_)
#
# plt.plot(range(1, 20), inertias, 'bx-')
# plt.xlabel('Values of K')
# plt.ylabel('Inertia')
# plt.show()

# best value => k = 8
k = 8

model = KMeans(n_clusters=k).fit(x)
centroids = model.cluster_centers_
labels = model.labels_

pickle.dump(model, open('final_model.sav', 'wb'))



