import json
import os
import pathlib

from nltk.stem.snowball import SnowballStemmer

STEMMER = SnowballStemmer('russian')

app_dir = pathlib.Path(__file__).parent.parent
words_with_stress_path = os.path.join(app_dir, 'stresses.json')
stems_with_stress_path = os.path.join(app_dir, 'stem_stresses.json')

with open(words_with_stress_path, 'r', encoding='utf-8') as fd:
    WORDS: dict = json.load(fd)

with open(stems_with_stress_path, 'r', encoding='utf-8') as fd:
    STEMS: dict = json.load(fd)
