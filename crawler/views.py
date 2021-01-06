from datetime import datetime
from django.shortcuts import render
import json

path = 'templates/static/'

def hello_world(request, query):
	with open(path + 'json/api.json', encoding = "utf-8") as jsonfile:
	    json_data = json.load(jsonfile)
	    if query == "Covid":
	    	index = 0
	    	img = 'images/cloud.jpg'
	    	file = 'javascript/visual.js'
	    if query == "Trump":
        	index = 1
        	img = 'images/cloud1.jpg'
        	file = 'javascript/visual2.js'
	    times1 = json_data['data'][index]['timesnews'][0]['topic']
	    times2 = json_data['data'][index]['timesnews'][1]['topic']
	    times3 = json_data['data'][index]['timesnews'][2]['topic']
	    tlink1 = json_data['data'][index]['timesnews'][0]['link']
	    tlink2 = json_data['data'][index]['timesnews'][1]['link']
	    tlink3 = json_data['data'][index]['timesnews'][2]['link']
	    yahoo1 = json_data['data'][index]['yahoo'][0]['topic']
	    yahoo2 = json_data['data'][index]['yahoo'][1]['topic']
	    yahoo3 = json_data['data'][index]['yahoo'][2]['topic']
	    ylink1 = json_data['data'][index]['yahoo'][0]['link']
	    ylink2 = json_data['data'][index]['yahoo'][1]['link']
	    ylink3 = json_data['data'][index]['yahoo'][2]['link']
	    gettime = json_data['data'][0]['gettime']
	    return render(request, 'home.html', {
	    	'search': query,
	        'times1': times1,
	        'times2': times2,
	        'times3': times3,
	        'tlink1': tlink1,
	        'tlink2': tlink2,
	        'tlink3': tlink3,
	        'yahoo1': yahoo1,
	        'yahoo2': yahoo2,
	        'yahoo3': yahoo3,
	        'ylink1': ylink1,
	        'ylink2': ylink2,
	        'ylink3': ylink3,
	        'img' : img,
	        'datetime': gettime,
	        'file' : file
	    })

