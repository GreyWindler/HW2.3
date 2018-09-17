import json
from pprint import pprint
with open('newsafr.json') as js_news:
  
  word = json.load(js_news)
  
  
import xml.etree.elementtree as ET
tree = ET.parse('newsafr.xml')
