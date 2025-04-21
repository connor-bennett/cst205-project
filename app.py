# Imports
#testing julians branch

from flask import Flask
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from PIL import Image, ImageOps 

import os
import random

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


# Routes
@app.route('/')
def hello():
    return render_template('index.html')