#!/usr/bin/python
import json
import xmltodict

def load_json(fname):
    with open(fname) as f:
        return words_to_list(json.load(f))

def load_xml(fname):
    with open(fname) as fd:
        return words_to_list_xml(xmltodict.parse(fd.read()))

def words_to_list(data):
    s = ''
    for item in data['rss']['channel']['items']:
        s += ' ' + item['description']
    return s.split()

def words_to_list_xml(data):
    s = ''
    for item in data['rss']['channel']['item']:
        s += ' ' + item['description']
    return s.split()

def filt(lst, length):
    return [el for el in lst if len(el) > length]

def count(lst):
    res_dct = {}
    for word in lst:
        if word in res_dct.keys():
            res_dct[word] += 1
        else:
            res_dct[word] = 1
    return res_dct.items()

def do_the_trick(lst):
    lst = filt(lst, 6)
    counted = count(lst)
    sorted_words = [word for word, co in sorted(counted, key=lambda x: x[1])]
    print(sorted_words[-3:])

data = load_json('newsafr.json')
do_the_trick(data)

data = load_xml('newsafr.xml')
do_the_trick(data)

