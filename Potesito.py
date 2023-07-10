import speech_recognition as sr
import subprocess
import PyPDF2
import pyttsx3
import sys
from playsound import playsound
from os.path import exists as file_exists
import openai
#from IPython.display import display, Markdown
#import yfinance as yf



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
    





def answer(textDetected):
    comands = {
            'test' :  convert_text_to_audio(TEST, 'test' , rate=150, volume=1.0, voice=1),
            'hi' : convert_text_to_audio(HI, 'hi' , rate=150, volume=1.0, voice=1),
            'bob' :  convert_text_to_audio(ACTIVE, 'bob' , rate=150, volume=1.0, voice=1),
            #'bob' : subprocess.check_call(['python','bob.py']),
            #'Spider-Man' : subprocess.check_call(['python','SpiderTema.py']),
            'question' : GenerateResponse(textDetected),
        }
    text = textDetected.split(" ")
    for word in text:
        print(word)
        if word in comands.keys():
            print('detected,\nProceed to respond')              
            filename = word + '.wav'
            if file_exists(filename):
                return filename
            else:
                print('generating...')
                comands[word]
    

if __name__ == "__main__":
    cad = speech()
    try:
        playsound(answer(cad))
    except:
        playsound('question.wav')
    
    
    

    
