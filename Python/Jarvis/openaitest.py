#!/usr/bin/env python3

import os 
import openai 
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davici-003",
  prompt=" Write something... ",
  temperature=0.7,
  max_token=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0 
)
  
  
  
  
  
  