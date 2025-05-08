# Imports
#testing julians branch

from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5
from PIL import Image, ImageOps 

import os
import random

app = Flask(__name__)
bootstrap = Bootstrap5(app)


# Routes
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/detail')
def detail():
    return render_template('detail_page.html')

if __name__== "__main__":
    app.run(debug==True)