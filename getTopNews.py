import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

path = 'templates/static/'

with open(path + 'json/api.json', encoding = "utf-8") as jsonfile:
	json_data = json.load(jsonfile)

time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def getTime(query, num):
	res = requests.get('https://time.com/search/?q='+query)
	if res.status_code == requests.codes.ok:
		soup = BeautifulSoup(res.text, 'html.parser') 
		index = 0
		stories = soup.find_all('div', class_='headline')
		for s in stories[1:4]:
			print("title: "+ s.text)
			print("url: "+ s.find('a').get('href'))
			json_data['data'][num]['timesnews'][index]['topic'] = s.text
			json_data['data'][num]['timesnews'][index]['link'] = s.find('a').get('href')
			index += 1

def getYahoo(query, num):
	res = requests.get('https://tw.news.yahoo.com/search?p='+query)
	if res.status_code == requests.codes.ok:
		soup = BeautifulSoup(res.text, 'html.parser') 
		index = 0
		stories = soup.find_all('h3')
		for s in stories[:3]:
			print("title: "+ s.text)
			print("url: "+ s.find('a').get('href'))
			json_data['data'][num]['yahoo'][index]['topic'] = s.text
			json_data['data'][num]['yahoo'][index]['link'] = 'https://tw.news.yahoo.com'+s.find('a').get('href')
			index += 1


getTime('Covid', 0)
getTime('Trump', 1)
getYahoo('Covid', 0)
getYahoo('川普', 1)
json_data['data'][0]['gettime'] = time_now

ret = json.dumps(json_data)
with open(path + 'json/api.json', 'w') as fp:
    fp.write(ret)