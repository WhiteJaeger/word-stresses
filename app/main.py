from flask import Flask, json
from flask_cors import CORS, cross_origin

from app.constants import WORDS

APP = Flask(__name__)
cors = CORS(APP)
APP.config['CORS_HEADERS'] = 'Content-Type'


@APP.route('/')
def home_view():
    return '<h1>Hello There!</h1>'


@APP.route('/get_word_stress/<string:word>')
@cross_origin()
def get_word_stress(word: str):
    return json.dumps({
        'word': word,
        'stress': WORDS[word] if word in WORDS else None
    }, ensure_ascii=False)
