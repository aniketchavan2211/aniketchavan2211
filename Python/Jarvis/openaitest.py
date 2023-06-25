#!/usr/bin/env python3

import os 
import openai 

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davici-003",
  prompt=" Write something... ",
  temperature=0.7,
  max_token=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0 
)
  
  
  
  
  
  