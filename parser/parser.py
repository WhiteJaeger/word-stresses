import json

import requests
from bs4 import BeautifulSoup

URLS = [
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-a.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-b.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-v.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-g.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-d.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-e.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-jo.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-zh.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-z.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-i.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-j.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-k.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-l.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-m.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-n.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-o.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-p.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-p_pe-pz.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-p_-pi-pn.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-p_po-pok.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-p_pol-poja.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-p_pra-pri.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-p_pro-prja.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-p_ps-pja.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-r.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-s.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-t.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-y.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-f.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-x.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-cs.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-ch.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-sh.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-sch.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-ji.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-je.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-jy.htm',
    'https://povto.ru/books/slovari/orfograficheskiy-slovar-online/orfograficheskii-slovar-online-bukva-ja.htm',
]

words = {}

for URL in URLS:
    response = requests.get(URL)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.content, "html.parser")
    words_html = soup.find_all('p')

    for w in words_html:
        word_html = str(w.find_next('em'))
        if not word_html or '<b>' not in word_html:
            continue
        word_html = word_html.replace('<em>', '')
        word_html = word_html.replace('</em>', '')
        word_html = word_html.replace('<b>', '|')
        word_html = word_html.replace('</b>', '')
        stressed_vowel_position = word_html.find('|')
        word = word_html.replace('|', '').lower()
        if word in words:
            continue
        words[word] = stressed_vowel_position


with open('./stresses.json', 'w', encoding='utf-8') as fd:
    print(len(words))
    json.dump(words, fd, ensure_ascii=False)
