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
        "headline": data["title"],
        "image": data["image"],
        "caption": data["caption"],
        "article": data["article"],
    }     
