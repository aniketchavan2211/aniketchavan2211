#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
  return " Hello flask "

app.run(host="0.0.0.0", port=5901)
