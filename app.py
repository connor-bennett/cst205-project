# Imports
#testing julians branch

from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5
from PIL import Image, ImageOps 

import os
import random

from backend import birds

app = Flask(__name__)
bootstrap = Bootstrap5(app)


# Routes
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/detail/<img_name>')
def detail(img_name):
    bird_data = birds.bird_data
    return render_template('detail_page.html', img_name=img_name, bird_info=bird_data)

if __name__== "__main__":
    app.run(debug==True)