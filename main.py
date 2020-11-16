import flask
from flask import request
import pandas as pd
import random
data = pd.read_csv('data.csv', names=['title', 'link', 'author', 'date',
                                      'datescraped', 'image', 'imagecaption', 'page', 'article'])
                            
app = flask.Flask(__name__)

@app.route('/headline', methods=['GET'])
def home():
    return random.choice(data.title)      
