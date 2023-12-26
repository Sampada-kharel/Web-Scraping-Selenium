import spotipy
from spotipy.oauth2 import SpotifyOAuth
from main import date,songs
from pprint import pprint
client_id="236e81bf0fc04f7bbd77e5526d251051"
client_secret="bc88f000f5384d8eb4cb17790686593a"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri="https://example.com",
                                               scope="playlist-modify-private",
                                               cache_path="token.txt"))

song_uris=[]
year=date[0:4]
for song in songs:
 result=(sp.search(q=f"track:{song} year:{year}", type='track'))
 try:
  uri=result["tracks"]["items"][0]["uri"]
  song_uris.append(uri)
 except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist= sp.user_playlist_create(user = sp.current_user()['id'],name = "top 100 billboard " + year,public = False)
sp.user_playlist_add_tracks(user=sp.current_user()['id'],playlist_id=playlist['id'],tracks=song_uris)

  


