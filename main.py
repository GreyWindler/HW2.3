f=open('/home/mmstepanov/git/py-homeworks-new/2.3.formats.json.xml/files/newsafr.json')
f=f.read()
json_loads = json.loads(f)
uniq_word=[]
for i in json_loads['rss']['channel']['items']:
	for word in i['description'].split(" "):
		if word not in uniq_word and len(word)>6:
			uniq_word.append(word)
  
  
import xml.etree.elementtree as ET
tree = ET.parse('newsafr.xml')
