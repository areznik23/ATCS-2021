import requests as req

from auth import access_token

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

r = req.get('https://api.spotify.com/v1/search?q=name:abc&type=playlist', headers=headers)
r = r.json()
new_id = r['playlists']['items'][1 ]['id']
print(new_id)
r = req.get('https://api.spotify.com/v1/playlists/' + new_id, headers=headers)
print(r.json())
