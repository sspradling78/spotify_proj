import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from os import getenv
from collections import OrderedDict
import pprint
import time

'''Getting API keys'''
key = getenv('CLIENT_ID')
secret = getenv('CLIENT_SECRET')

'''Connection to Spotify'''
client_credentials_manager = SpotifyClientCredentials(
    client_id=key, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

url = 'https://open.spotify.com/'


def get_artist(artist_search):
    '''Getting Artist Information'''
    result_artist_search = sp.search(artist_search, type='artist', market='US')
    artists_result = result_artist_search['artists']['items']
    artist = 0
    for number in range(len(artists_result)):
        if artists_result[number]['name'] == artist_search:
            artist = number
        else:
            pass
    artist_result = artists_result[artist]
    return artist_result