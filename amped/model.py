from movies import movies
from pandas import json_normalize
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pickle

movies = json_normalize(movies)

def scale_data():
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
    return x

# Resource: referenced our work in kmeans_clustering.py for class
# optimal k value = 8
def get_optimal_k():
    inertias = []
    for k in range(1, 20):
        kmeanModel = KMeans(n_clusters=k).fit(x)
        inertias.append(kmeanModel.inertia_)

    plt.plot(range(1, 20), inertias, 'bx-')
    plt.xlabel('Values of K')
    plt.ylabel('Inertia')
    plt.show()

# Resource: https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/
def save_model(model):
    pickle.dump(model, open('final_model.sav', 'wb'))

# best value => k = 8
def main():
    k = 8
    x = scale_data()
    model = KMeans(n_clusters=k).fit(x)
    save_model(model)

main()




