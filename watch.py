import sys
import os
import subprocess
import time
import logging

htmlContentPre = """
<html>
<head>
<style>
	audio { width: 100%;}
</style>
</head>
<body>
<audio controls autoplay loop>
<source src='"""

htmlContentPost = """'>
</audio>
</body>
</html>
"""

try :
	while True:
		time.sleep(2)
		temp = open("status", "r")
		text = temp.readline()
		if "yes" not in text:
			continue
		file = open('myfile', 'r')
		url = file.readline()
#			print len(url)
		if (len(url) > 0):
			link = "youtube-dl -f bestaudio -o outfile.%(ext)s " + url
			print "Downloading file at ", link
			# os.system(link)
			link = link.split(' ')
			
			# removing any previously available file
			somelist = os.listdir(os.getcwd())
			filename = [x for x in somelist if "outfile" in x]
			if (len (filename) > 0):
				filename = filename[0]
				if ".part" not in filename:
					os.remove(filename+'.part')
		
			# creating process for youtube-dl
			subprocess.call(link)
			somelist = os.listdir(os.getcwd())
			filename = [x for x in somelist if "outfile" in x] [0]
			if ".part" not in filename:
				os.rename(filename, filename+'.part')
			print "iteration completed"
			htmlContent = htmlContentPre + filename + '.part' + htmlContentPost
			htmlfile = open('index.html', 'w')
			htmlfile.write(htmlContent)
			htmlfile.close()
			print "html generated"
			del htmlfile
			del htmlContent
			temp.close()
			temp = open("status", "w+")
			temp.close()
			del link
			del somelist
			del filename
		file.close()
		del temp
		del file
except KeyboardInterrupt:
		#observer.stop()
		exit(0)

observer.join()
