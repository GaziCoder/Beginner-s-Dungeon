
import pyaudio

import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print (voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
     speak('hi, I am genius')

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if  hour>= 0 and hour<12:
         speak('Good Morning! Ariba Mam')

    elif hour>= 12 and hour<16:
         speak('Good Afternoon! Ariba Mam')

    else:
      speak('Good evening! Ariba Mam')   

def askMe():
      speak('What can i do for you?')
wishMe()
askMe()

def takeCommand():
    ''' if u are a proprogrammer u will get this func \
     or else neverrrrrr '''
r = sr.Recognizer()
with sr.Microphone() as source:
     print('Listening.......!')
     r.pause_threshold = 1
     audio = r.listen(source)

     try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

     except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        












   




