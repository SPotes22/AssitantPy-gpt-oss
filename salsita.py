from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
import webbrowser
import pyautogui
from time import sleep

flag = 0
client_id = "YOUR_SPOTIFY_ID"
client_secret = "YOUR_SPOTIFY_SECRET"
artist = 'Adalberto Santiago'
song = "La noche mas linda"

if len(artist) > 0:
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
    result = sp.search(q=song, type='track', limit=50)
    
    for track in result['tracks']['items']:
        artists = [artist['name'] for artist in track['artists']]
        if artist in artists:
            flag = 1
            webbrowser.open(track['uri'])
            sleep(5)
            pyautogui.press("enter")
            break  # Exit the loop once a matching song is found

if flag == 0:
    formatted_song = song.replace(" ", "%20")
    webbrowser.open(f'spotify:search:{formatted_song}')
    sleep(5)
    for _ in range(22):
        pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("enter")
