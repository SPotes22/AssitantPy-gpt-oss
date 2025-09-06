import speech_recognition as sr
import subprocess
import PyPDF2
import pyttsx3
import sys
import webbrowser
from playsound import playsound
from  os import remove 
from os.path import exists as file_exists
import openai
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
import webbrowser
import pyautogui
from time import sleep


class Error():
    def __init__(self,error_name,details):
        self.error_name = error_name
        self.details = details

class AudioGenerationError(Error):
    def __init__(self,details):
        super().__init__("Audio error,Try Running The Script again.\nError saving audio file: ", details)    


#BOT NAME S9B2
def speech():
    # Esta funcion retorna una cadena 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something")
        audio = r.listen(source)
        print("Recognizing Now .... ")
        # recognize speech using google
        try:
            inpu = r.recognize_google(audio)
            #print("You have said \n" + inpu)
            print("Audio Recorded Successfully \n ")
        except Exception as e:
            print("Error :  " + str(e))
        # write audio
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())
        return inpu


def convert_text_to_audio(text, output_file, rate=150, volume=1.0, voice=None):
    #Function to convert the extracted text into an audio file using pyttsx3:
    engine = pyttsx3.init()
    
    if voice:
        '''i Used this as a bool value, For more information on the type of bot voice check pyttsx3 Docs'''
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voice].id)
    
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    engine.save_to_file(text, output_file + '.wav')
 
    # Wait until above command is not finished.
    engine.runAndWait()
    return None

USERNAME = 'master Potes'
TEST = 'test complete'
HI = f'Hello {USERNAME}'
ACTIVE = "that's my name. at your service"
KEY = open('.key').read()
RESULT = 'I have finished searching on YouTube. Based on your query, I found these videos that might interest you. Feel free to check it out!'

def GenerateResponse(text):
    openai.api_key = KEY
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature = 0.7,
        max_tokens = 240,
    )
    
    answer = response.choices[0].text
    print(answer)
    convert_text_to_audio(answer, 'question' , rate=150, volume=1.0, voice=1)


def YTsearch():
    search = speech() #input('enter the topic and thing you want to search on YT: ')
    if len(search) > 0:
        search_query = search
        youtube_search_url = f"https://www.youtube.com/results?search_query={search_query}"
        webbrowser.open(youtube_search_url)
    if file_exists('YouTube.wav'):
        return 'result.wav'
    else:
        convert_text_to_audio(RESULT, 'YouTube', rate=150, volume=1.0, voice=1),
        return 'YouTube.wav'


def Spiderman():
    flag = 0
    client_id = "YOUR_SPOTIFY_ID"
    client_secret = "YOUR_SPOTIFY_SECRET"
    artist = 'Alicia Keys'
    song = "it's on again"

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

def Salsa():
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

def answer(textDetected):
    comands = {
        'test': convert_text_to_audio(TEST, 'test', rate=150, volume=1.0, voice=1),
        'hi': convert_text_to_audio(HI, 'hi', rate=150, volume=1.0, voice=1),
        'Bob': convert_text_to_audio(ACTIVE, 'bob', rate=150, volume=1.0, voice=1),
        'question': GenerateResponse(textDetected),
        'salsa' : Salsa,# subprocess.check_call(['python','salsita.py']),
        'Spider-Man' : Spiderman, #subprocess.check_call(['python','SpiderTema.py']),
        'YouTube' : YTsearch,#subprocess.check_call(['python','ytTest.py']),
    }
    comand_keys = comands.keys()
    text = textDetected.split(" ")

    for word in text:
        if (word in comand_keys):
            print('Detected command:', word)
            filename = word + '.wav'
            if file_exists(filename):
                return filename
            else:
                print('Generating...')
                comands[word]()
                return  filename
        else:
            print('this is not a comand')
    return None 
    

if __name__ == "__main__":
    remove('YouTube.wav')
    cad = speech()
    try:
        playsound(answer(cad))
    except:
        playsound('question.wav')
        

    

