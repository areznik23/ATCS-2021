import pandas as pd

# file for organizational purposes, export of the titles for the movies
data = pd.read_csv('imdb_top_1000.csv')

titles = data['Series_Title']
