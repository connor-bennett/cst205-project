# Imports
from flask import Flask
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5
from image_info import image_info
from PIL import Image, ImageOps 
import os
import random

# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Routes
@app.route('/')
def hello():
    shuffled = image_info[:]
    random.shuffle(shuffled)
    selected = shuffled[:3]
    return render_template('index.html', images=selected)