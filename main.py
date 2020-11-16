import flask
from flask import request
import pandas as pd
import random
data = pd.read_csv('data.csv', names=['title', 'link', 'author', 'date',
                                      'datescraped', 'image', 'imagecaption', 'page', 'article'])
                            
app = flask.Flask(__name__)

@app.route('/news_article', methods=['GET'])
def home():
    return {
        "headline": random.choice(data.title),
        "image": random.choice(data.image),
        "caption": random.choice(data.imagecaption),
        "article": random.choice(data.article),
    }     
