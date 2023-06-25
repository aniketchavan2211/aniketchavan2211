#!/usr/bin/env python3

# speech recognition specific in MacOS, use other library for Windows and Linux.

import speech_recognition as sr
import os
import webbrowser
import openai
import datetime

def say(text):
  os.system(f" say {text} ")

def takeCommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.pause_threshold = 0.6
    audio = r.listen(source)
    try:
      print("Recognizing...")  
      query = r.recognize_google(audio, language="en-in")
      print(f"User said:  {query}")
    except Exception as e:
      return "Some Error Occurred. Sorry from Jarvis."
    
if __name__ == '__main__':
  print("Hello")
  say("Hey there, I'm Jarvis")
  while True:
    print("Listening...")
    query = takeCommand()
    sites = ["youtube.com", "wikipedia.com"]
    for site in sites:
      if f"Open {site[0]}.lower()" in query.lower():
        say("Opening site[0]")
        webbrowser.open(site[1])
      
    if "Open music" in query:
        musicPath = "Path/to/Music"
        os.system(f"open {musicPath}")
      
    if "the time" in query:
        musicPath = "Path/to/Music"
        strfTime = datetime.datetime.now().strftime("%H:%M:%S")
        say(f"time is {strfTime}")
        
    if "open facetime".lower()  in query.lower():
      os.system(f"open /System/Application/FaceTime.app")
      
  # say(query)