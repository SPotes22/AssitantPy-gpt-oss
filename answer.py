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
client_id = "3814284cc64f49f582a7f9c87374edc2"
client_secret = "7681d1b27c6c42cda5f0f49ab16ac657"

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


