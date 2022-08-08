from typing import Optional

from flask import Flask, json
from flask_cors import CORS, cross_origin

from app.constants import WORDS, STEMS, STEMMER

APP = Flask(__name__)
cors = CORS(APP)
APP.config['CORS_HEADERS'] = 'Content-Type'


@APP.route('/')
def home_view():
    return '<h1>Hello There!</h1>'


@APP.route('/get_word_stress/<string:word>')
@cross_origin()
def get_word_stress(word: str):
    stress_position = None

    stemm = STEMMER.stem(word)

    if word in WORDS:
        stress_position = WORDS[word]
    elif stemm in WORDS:
        stress_position = WORDS[stemm]
    elif stemm in STEMS:
        stress_position = STEMS[stemm]
    else:
        sub_word = find_similar_word_by_substring(word)
        if sub_word:
            stress_position = WORDS.get(sub_word) or STEMS.get(sub_word)

    return json.dumps({
        'word': word,
        'stress': stress_position
    }, ensure_ascii=False)


def find_similar_word_by_substring(word: str) -> Optional[str]:
    for length in range(len(word) - 1, 0, -1):
        if length <= 3:
            break
        sub_word = word[0:length]
        if sub_word in WORDS or sub_word in STEMS:
            return sub_word
