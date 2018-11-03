import os 
import re
import requests
from datetime import datetime

TRELLO_KEY = os.environ['TRELLO_KEY']
TRELLO_TOKEN = os.environ['TRELLO_TOKEN']
queryStr = {'key': TRELLO_KEY, 'token': TRELLO_TOKEN}
print(TRELLO_KEY, TRELLO_TOKEN)

p = re.compile('\\*\\*Venue Address:\\*\\* ([^*]+)')

url = 'https://api.trello.com/1/lists/589b59c5048da67fae2392a9/cards'
response = requests.get(url, params=queryStr)
cardList = response.json()
print(len(cardList))
events = []
for card in cardList:
	name = card['name']
	desc = card['desc']
	'''unformDate = card['due']
	eventDate = unformDate.split('T')[0]
	dueDate = datetime.strptime(eventDate,'%Y-%m-%d')
	url = card['url']'''
	matches = p.findall(desc)
	if len(matches) == 0:
		print("No location")
		continue
	location = matches[0]
	addr = location.rstrip('\n')
	events.append((name, addr))
	#print(name, dueDate, '<a href=',url,'/><br>')

HERE_ID = '1UIAmImGFkEOuqSWrqZB'
HERE_CODE = '4U0I9kqvWeZgSn55e3b-6Q'

here_url = '''https://geocoder.api.here.com/6.2/geocode.json
			?app_id=1UIAmImGFkEOuqSWrqZB&app_code=4U0I9kqvWeZgSn55e3b-6Q&searchtext='''
successfuls = []
for e in events:
	currAddr = e[1]
	print(currAddr)
	#print('\t searching for addr: ', currAddr)
	#here_url.format(ID= HERE_ID, CODE = HERE_CODE, ADDR = currAddr)
	hereResp = requests.get(here_url + currAddr)
	if hereResp.status_code != 200:
		#print(hereResp.url)
		continue
	hereJson = hereResp.json()
	longLatt = hereJson['Response']['View'][0]['Location']['DisplayPosition']
	successfuls.append[longLatt]
	print(longLatt)

s = 'https://geocoder.api.here.com/6.2/geocode.json?app_id=1UIAmImGFkEOuqSWrqZB&app_code=4U0I9kqvWeZgSn55e3b-6Q&searchtext=200%20S%20Mathilda%20Sunnyvale%20CA'
'''
card_url = 'https://api.trello.com/1/cards/5bb1389e05793651631b2180/checklists'
response = requests.get(card_url, params=queryStr)
print(response.text)
'''

'''
actions = 'https://api.trello.com/1/cards/5b75bc451868528bc44603dc/actions'
response = requests.get(actions, params=queryStr)
print(response.text)
'''