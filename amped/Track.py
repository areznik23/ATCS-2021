"""
Amped Music/Movie Project

@author: Alex Reznik
@version: 10 May 2022
"""

# Track object for operations with a single song
class Track:

    def __init__(self, id, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo):
        self.id = id
        self.danceability = danceability
        self.energy = energy
        self.key = key
        self.loudness = loudness
        self.mode = mode
        self.speechiness = speechiness
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.valence = valence
        self.tempo = tempo

    # Format method to align with the amped.py file standards for operation
    def format(self):
        return {
            'track_id': self.id,
            'audio_features': {
                'audio_features.danceability': self.danceability,
                'audio_features.energy': self.energy,
                'audio_features.key': self.key,
                'audio_features.loudness': self.loudness,
                'audio_features.mode': self.mode,
                'audio_features.speechiness': self.speechiness,
                'audio_features.acousticness': self.acousticness,
                'audio_features.instrumentalness': self.instrumentalness,
                'audio_features.liveness': self.liveness,
                'audio_features.valence': self.valence,
                'audio_features.tempo': self.tempo
            }
        }