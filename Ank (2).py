import pyttsx3
import speech_recognition as sr
import webbrowser
import smtplib
import os


ggi = pyttsx3.init('sapi5')
voices = ggi.getProperty('voices')
ggi.setProperty('voice', voices[0].id)

def speak(audio):
    ggi.say(audio)
    ggi.runAndWait()
def myCommand():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("i am logan,ready for ypur next command")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
        
    try:
        command=r.recognize_google(audio)
        print('you said'+command+'/n')
        
        #loop back to continiu to listien again
    except sr.UnknownValueError:
        assistant(myCommand())
        
    return command



        
#if statement to talk logan

def assistant(command):
    if 'who are you' in command:
        speak('i am logan,your friend')
        
    if 'how are you' in command:
        speak('i am rocking')
    if 'who made you' in command:
        speak('justinashu made me')

speak('i am ready for your next command')

while True:
    assistant(myCommand())