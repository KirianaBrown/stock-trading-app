import os
from app import app
from flask import Flask, render_template

from dotenv import load_dotenv
load_dotenv()

@app.route("/")
def index():
  return render_template('./layout.html')