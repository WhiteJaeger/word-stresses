import json
import pathlib
import os

app_dir = pathlib.Path.cwd()
word_with_stress_path = os.path.join(app_dir, 'stresses.json')

with open(word_with_stress_path, 'r', encoding='utf-8') as fd:
    WORDS = json.load(fd)
