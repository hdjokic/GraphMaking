import json
import os
def xyFormater(xaxis, yaxis, inputFile, outputFile):
	with open(inputFile, 'r') as f:
		with open(outputFile, 'w') as o:
			
			planets=json.load(f)
			for planet in planets:
				if(planet[xaxis]!=None and planet[yaxis]!=None):
					#js= json.loads(planet)
					xystr = (str(planet[xaxis]) +" "+ str(planet[yaxis]))
					o.write(xystr)
					o.write('\n')
			#print(planets2['pl_name'])
			#with open('data.json', 'w') as j:
			#	for line in f:
			#		line = line.rstrip("]\n").lstrip("[")
			#		j.write(line)
				
			#with open('data.json', 'r') as j:
			#	planets = json.load(j)
			#	print(planets[pl_name])
#xyFormater(xaxis, yaxis, "data.txt", "xy.txt")

