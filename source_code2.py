# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:46:35 2019

@author: HP
"""
from gtts import gTTS
import speech_recognition as sr
import webbrowser
import smtplib
import os


def talkTome(audio):
    print(audio)
    tts=gTTS(text=audio,lang='en')
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3")
    return tts



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
        talkTome('i am logan,your friend')
        
    if 'how are you' in command:
        talkTome('i am rocking')
    if 'who made you' in command:
        talkTome('justinashu made me')

talkTome('i am ready for your next command')

while True:
    assistant(myCommand())