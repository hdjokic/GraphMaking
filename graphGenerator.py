import subprocess
import os

def f(command, filename, xaxis, yaxis):
	with open('xy.txt', 'r') as file:
		p = subprocess.Popen(['gnuplot'], shell = True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')

		p.stdin.write("set term png size 640,480\n")
		p.stdin.write("set output \"scatterPlot.png\"\n")
		p.stdin.write("set title \"" +yaxis+ " as a fnc of "+ xaxis + "\" noenhanced\n")
		p.stdin.write(command +" \""+ filename+ "\" with points pt 1\n")
		p.stdin.write("quit")
		status = "{\"status\":\"success\",\"imageFilename\":\"scatterPlot.png\",\"height\":360,\"width\":480}\r\n"
		print(status, flush = True)
		
		#set output scatterPlot.png
		#xaxis=xaxis.encode('utf-8')
		#yaxis=yaxis.encode('utf-8')
		#command=command.encode('utf-8')
		#filename=filename.encode('utf-8')

		#p.communicate("""
		#set term png size 640,480
		#set output scatterPlot.png
		#set title """ +xaxis + """ as a fnc of """ +yaxis +"""
		#""" + command + " " + filename + """ with points pt 1
		#""".encode('utf-8'))
#		p.communicate(b'set term png size 640,480\nset output scatterPlot.png')

		#p.communicate(b'set output scatterPlot.png')
		#p.communicate("set title " + xaxis + " as a fnc of " +yaxis )
		#p.communicate(command + filename + " with points pt 1")

#with open('data.txt') as file:
#f(command, 'xy.txt', xaxis, yaxis)
#get json
