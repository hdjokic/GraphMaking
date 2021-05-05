import xyFormater
import graphGenerator

def getCommands():
	inp = input("Enter the values or quit: ")
	#command = list(inp.keys())[0]
	#print(inp)
	Dict = eval(inp)
	#print(Dict)

	#if Dict.get(command) is None:
	#	print("command does not exist")
	
	while (Dict.get("command") != "quit"):
		command = Dict.get("command")
		xaxis = Dict.get("xAxis")
		yaxis = Dict.get("yAxis")
		
		xyFormater.xyFormater(xaxis, yaxis, "data.txt", "xy.txt")
		graphGenerator.f(command, 'xy.txt', xaxis, yaxis)

		#status = "{\"status\":\"success\",\"imageFilename\":\"scatterPlot.png\",\"height\":360,\"width\":480}\r\n"
		#print(status, flush = True)
		inp = input("Enter the values or quit: ")
		Dict = eval(inp)
	status = "{\"status\":\"quit\"}"
	print(status, flush = True)



	
