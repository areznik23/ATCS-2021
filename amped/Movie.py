class Movie:
    def __init__(self, title, id):
        self.title = title
        self.id = id
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track.format())

    def format(self):
        return {'title': self.title, "tracks": self.tracks}