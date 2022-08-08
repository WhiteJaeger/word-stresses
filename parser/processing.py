from nltk.stem.snowball import SnowballStemmer

import json
import pathlib
import os


if __name__ == '__main__':

    stemmer = SnowballStemmer('russian')

    app_dir = pathlib.Path(__file__).parent.parent
    word_with_stress_path = os.path.join(app_dir, 'stresses.json')
    with open(word_with_stress_path, 'r', encoding='utf-8') as fd:
        WORDS: dict = json.load(fd)

    stem_with_stress_path = os.path.join(app_dir, 'stem_stresses.json')
    STEMS_WITH_STRESSES = {}
    for word, stress_position in WORDS.items():
        STEMS_WITH_STRESSES[stemmer.stem(word)] = stress_position
    
    with open(stem_with_stress_path, 'w', encoding='utf-8') as fd:
        json.dump(STEMS_WITH_STRESSES, fd, ensure_ascii=False)
