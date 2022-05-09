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

    def format(self):
        return {
            'track_id': self.id,
            'audio_features': {
                'danceability': self.danceability,
                'energy': self.energy,
                'key': self.key,
                'loudness': self.loudness,
                'mode': self.mode,
                'speechiness': self.speechiness,
                'acousticness': self.acousticness,
                'instrumentalness': self.instrumentalness,
                'liveness': self.liveness,
                'valence': self.valence,
                'tempo': self.tempo
            }
        }