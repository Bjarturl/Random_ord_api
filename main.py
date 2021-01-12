import flask
from flask import request
from helpers import get_random_word_from_file
from flask_cors import CORS, cross_origin
app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/random_ord', methods=['GET'])
@cross_origin()
def home():
    word = get_random_word_from_file()
    return {
        "ord": word.strip()
    }     

if __name__ == "__main__":
    app.run(debug=False)