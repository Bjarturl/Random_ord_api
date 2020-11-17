import flask
from flask import request
import pandas as pd
import random
from newsGenerator import getRandomNews

app = flask.Flask(__name__)

@app.route('/news_article', methods=['GET'])
def home():
    data = getRandomNews()
    return {
        "headline": random.choice(data["title"]),
        "image": random.choice(data["image"]),
        "caption": random.choice(data["caption"]),
        "article": random.choice(data["article"]),
    }     
