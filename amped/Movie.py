import statistics as stat

class Movie:
    def __init__(self, title, id):
        self.title = title.replace('+', ' ')
        self.id = id
        self.tracks = []
        self.formatted_tracks = []
        self.danceability = []
        self.energy = []
        self.key = []
        self.loudness = []
        self.mode = []
        self.speechiness = []
        self.acousticness = []
        self.instrumentalness = []
        self.liveness = []
        self.valence = []
        self.tempo = []

    def add_track(self, track):
        self.tracks.append(track)
        self.formatted_tracks.append(track.format())

    def aggregate_audio_features(self):
        for track in self.tracks:
            self.danceability.append(track.danceability)
            self.energy.append(track.energy)
            self.key.append(track.key)
            self.loudness.append(track.loudness)
            self.mode.append(track.mode)
            self.speechiness.append(track.speechiness)
            self.acousticness.append(track.acousticness)
            self.instrumentalness.append(track.instrumentalness)
            self.liveness.append(track.liveness)
            self.valence.append(track.valence)
            self.tempo.append(track.tempo)

    # reference source for this operation: https://www.geeksforgeeks.org/find-median-of-list-in-python/
    def set_median_audio_features(self):
        self.aggregate_audio_features()
        self.danceability = self.get_median(self.danceability)
        self.energy = self.get_median(self.energy)
        self.key = self.get_median(self.key)
        self.loudness = self.get_median(self.loudness)
        self.mode = self.get_median(self.mode)
        self.speechiness = self.get_median(self.speechiness)
        self.acousticness = self.get_median(self.acousticness)
        self.instrumentalness = self.get_median(self.instrumentalness)
        self.liveness = self.get_median(self.liveness)
        self.valence = self.get_median(self.valence)
        self.tempo = self.get_median(self.tempo)

    def get_median(self, l):
        return round(stat.median(l), 4)

    def format(self):
        return {'title': self.title, 'audio_features': {
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
            }}

    def model_format(self):
        return {'title': self.title, 'audio_features': {
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
        }}