import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from os import getenv
from collections import OrderedDict
import pprint
import time
import dateutil.parser

'''Getting API Keys'''
key = getenv('CLIENT_ID')
secret = getenv('CLIENT_SECRET')

client_credentials_manager = SpotifyClientCredentials(client_id=key, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

url = 'https://open.spotify.com/'

song_search = input("Enter a Song Title: ")

artist_search = input("By which artist: ")



'''Artist's info search'''
result_artist_search = sp.search(artist_search, type='artist', market='US')
artists_result = result_artist_search['artists']['items']

artist = 0
for number in range(len(artists_result)):
    if artists_result[number]['name'] == artist_search:
        artist = number
        print(artists_result[artist]['name'])
    else:
        pass

artist_result = artists_result[artist]

'''Artist's URL & Artist URI(for searching in app)'''
artist_url = artist_result['external_urls']['spotify']
artist_uri = artist_result['uri']

'''Artist name'''
artist_name = artist_result['name']

'''Artist Genre'''
artist_genre = artist_result['genres']

'''Getting list of albums from artist'''
artist_albums_info = sp.artist_albums(artist_uri, album_type='album', limit=50)
artist_albums = artist_albums_info['items']

list_of_albums = []

for album in range(len(artist_albums)):
    list_of_albums.append(artist_albums[album]['name'])
    
list_of_albums_no_dup = OrderedDict.fromkeys(list_of_albums)

t_t = sp.artist_top_tracks(artist_uri)
top_tracks = t_t['tracks']

list_of_top_tracks = []
list_of_top_tracks_urls = []
for top in range(len(top_tracks)):
    list_of_top_tracks.append(top_tracks[top]['name'])
    list_of_top_tracks_urls.append(top_tracks[top]['external_urls']['spotify'])

'''Track Search'''
song_search_result = sp.search(song_search, limit=50, type='track', market='US')
track_search_result = song_search_result['tracks']['items']

'''Testing song title with given artist'''
artist_num = 0
for i in range(len(track_search_result)):
    # print(track_search_result[i]['album']['artists'][0]['name'])
    if (track_search_result[i]['album']['artists'][0]['name'] == artist_search) & (track_search_result[i]['album']['total_tracks'] > 1):
        artist_num = i
    else:
        pass

'''First result from search list'''
track_search_first_result = track_search_result[0]

'''Track URL & ID'''
track_url = track_search_result[artist_num]['external_urls']['spotify']
track_id = track_search_result[artist_num]['id']

'''Album info'''
track_album = track_search_result[artist_num]
track_album_title = track_album['album']['name']
track_album_url = track_album['album']['external_urls']['spotify']
track_number = track_album['track_number']
track_release_date = dateutil.parser.isoparse(track_album['album']['release_date'])

'''Verified artist from search'''
track_artist = track_search_result[artist_num]['album']['artists'][0]['name']

'''Track length'''
track_length_sec = ((track_search_first_result['duration_ms']) / 1000)
track_length_min = int(track_length_sec // 60)
track_length_sec_rem = int(track_length_sec % 60)
track_time = time.strftime('%M:%S', time.gmtime(track_length_sec))

'''Check song if explicit'''
is_explicit = track_album['explicit']


# print(artist_search, "- Top tracks:")
print("")
# for i in range(len(list_of_top_tracks)):
#     pprint.pprint(list_of_top_tracks[i])
#     pprint.pprint(list_of_top_tracks_urls[i])
#     print("")

# pprint.pprint(track_album)
# print(artist_search, ":", track_album_title, "was released:", track_release_date)
# print(track_album_url)
# print()