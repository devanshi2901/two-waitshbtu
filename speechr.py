
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import pygame
from pygame import mixer


def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Say something!")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data


time.sleep(0.5)
print("Speak now . . .")
recordAudio()