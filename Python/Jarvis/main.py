#!/usr/bin/python3

# speech recognition specific in MacOS, use other library for Windows and Linux.

import speech_recognition as sr
import os
import webbrowser
import openai


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
  say(" Hello, I'm Jarvis")
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
      os.startfile(musicPath)

  # say(query)
