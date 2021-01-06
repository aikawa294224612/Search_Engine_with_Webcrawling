import requests
from bs4 import BeautifulSoup
import json

import matplotlib.pyplot as plt
import numpy as np
import jieba.analyse
import codecs
from wordcloud import WordCloud
from PIL import Image

path = 'templates/static/'

reducelist = ["How", "What", "Why", "Time", "TIME", '...', "Will", "Many", "19"]
mask = np.array(Image.open(path + 'images/mask.jpg'))

with open(path + 'json/rankapi.json', encoding = "utf-8") as jsonfile:
	json_data = json.load(jsonfile)

with open(path + 'json/rankapi2.json', encoding = "utf-8") as jsonfile2:
	json_data2 = json.load(jsonfile2)

def getTitle(query):	
	data = ''
	for i in range(10):
		res = requests.get('https://time.com/search/?q=' + query + '&page='+ str(i))
		if res.status_code == requests.codes.ok:
			soup = BeautifulSoup(res.text, 'html.parser') 
			stories = soup.find_all('div', class_='headline')
			for s in stories[:9]:
				data += (s.text +' ')
	print("Finish getting titles")
	return data


def generate_wordcloud(keywords, file_path):
    wc = WordCloud(font_path = path + 'msyh.ttf', background_color = "white",
                    max_words = 2000, width = 1200, height = 600, mask = mask)
    wc.generate_from_frequencies(keywords)
    plt.imshow(wc)
    plt.axis("off")
    plt.figure(figsize = (12, 8), dpi = 200)
    plt.show()
    wc.to_file(file_path)
    
def get_keywords(data, type, topN):
	i = 0
	keywords = {}
	tags = jieba.analyse.extract_tags(data, topK = topN, withWeight = True)
	for tag, weight in tags:
		if tag not in reducelist:
			keywords[tag] = weight
			if i<5:
				if type is 'C':
					json_data[i]['name'] = tag
					json_data[i]['text'] = tag
					json_data[i]['count'] = round(weight*10,1)
				else:
					json_data2[i]['name'] = tag
					json_data2[i]['text'] = tag
					json_data2[i]['count'] = round(weight*10,1)
				i += 1
	print("Finish getting keywords")
	return keywords
        

allCovidTitles = getTitle('Covid')
keywords_Covid = get_keywords(allCovidTitles, 'C',  30)
generate_wordcloud(keywords_Covid, path + "images/cloud.jpg")

allTrumpTitles = getTitle('Trump')
keywords_Trump = get_keywords(allTrumpTitles, 'T', 30)
generate_wordcloud(keywords_Trump, path + "images/cloud1.jpg")

ret = json.dumps(json_data)
ret2 = json.dumps(json_data2)
with open(path + 'json/rankapi.json', 'w') as fp:
    fp.write(ret)

with open(path + 'json/rankapi2.json', 'w') as fp:
    fp.write(ret2)

