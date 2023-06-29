#!/usr/bin/env python3

# speech recognition specific in MacOS, use other library for Windows and Linux.

import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import random

# AWS Code whisper 

chatStr = ""
def chat(prompt, chatStr):
  global chatStr
  openai.api_key = apikey
  text = f"OpenAI response for promot: {prompt} \n"
  prompt = f"Tony: {prompt}\n Jarvis"
  response = openai.Completion.create(
    model="text-davici-003",
    prompt=chatStr,
    temperature=0.7,
    max_token=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0 
) 
  # todo: Wrap this in try catch block
  # print(response["choices"[0]["text"])
  text += response["choices"][0]["text"]
  if not os.path.exists("Openai"):
    os.mkdir("Openai")
  
  # with open(f"Openai/prompt- {random.ranint(1, 6262737373)}",  "w") as f:
  with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
    f.write(text)

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
      
    elif "the time" in query:
        musicPath = "Path/to/Music"
        strfTime = datetime.datetime.now().strftime("%H:%M:%S")
        say(f"time is {strfTime}")
        
    elif "open facetime".lower()  in query.lower():
      os.system(f"open /System/Application/FaceTime.app")
    
    elif "Using artificial intelligence".lower() in query.lower():
      ai(prompt=query)
    
     else: 
       chat(query, chatStr)
       
  # say(query)