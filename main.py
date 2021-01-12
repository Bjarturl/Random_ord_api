import flask
from flask import request
from helpers import get_random_word_from_file

app = flask.Flask(__name__)
@app.route('/random_ord', methods=['GET'])
def home():
    word = get_random_word_from_file()
    return {
        "ord": word.strip()
    }     

if __name__ == "__main__":
    app.run(debug=False)