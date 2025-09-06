from selenium import webdriver
from selenium.webdriver.common.by import By
import webbrowser
import pyautogui
from time import sleep
from spotipy.oauth2 import SpotifyClientCredentials
#driver = webdriver.Chrome()
#driver.get('https://open.spotify.com/track/1lehjJeIwuFObvhBdD1R0c')
#pyautogui.press("enter")

link = 'https://open.spotify.com/track/1lehjJeIwuFObvhBdD1R0c'
song = link[24::]
print(song) 

flag = 0
client_id = "YOUR_SPOTIFY_ID"
client_secret = "YOUR_SPOTIFY_SECRET"

if flag == 0:
    song = song.replace(" ", "%20")
    webbrowser.open(f'spotify:search:{song}')
    #sleep(5)
    pyautogui.press("enter")
    '''
    for i in range(23):
        pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("enter")
    '''


