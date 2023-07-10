from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
import webbrowser
import pyautogui
from time import sleep


flag = 0
client_id = "3814284cc64f49f582a7f9c87374edc2"
client_secret = "7681d1b27c6c42cda5f0f49ab16ac657"
autor = 'jim groce'
song = "Time in a bottle".upper()


if len(autor) > 0:

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
    result = sp.search(autor)

    for i in range(0, len(result["tracks"]["items"])):
        name_song = result["tracks"]["items"][i]["name"].upper()
        if song in name_song:
            flag = 1
            webbrowser.open(result["tracks"]["items"][i]["uri"])
            sleep(5)
            pyautogui.press("enter")

if flag == 0:
    song= song.replace(" ", "%20")
    webbrowser.open(f'spotify:search:{song}')
    sleep(5)
    for i in range(28):
        pyautogui.press("tab")  
    pyautogui.press("enter")