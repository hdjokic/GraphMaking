import urllib.request
import urllib
import json
import sys
import getCommands

def calTech():
	file = open("jsonValue.txt", "w+")
	url = sys.argv[1]
	response = urllib.request.urlopen(url)
	data = json.loads(response.read())

	with open('data.txt', 'w') as outfile:
		json.dump(data, outfile)
		#print(data)

calTech()
getCommands.getCommands()
