import sys
import os
import subprocess
import time

try :
	while True:
		time.sleep(2)
		file = open("myfile", "r")
		text = file.readline()
		# print "file has  ", text
		if len(text) == 0:
			file.close()
			del file
			continue
		# file = open('myfile', 'r')
		url = text
#			print len(url)
		if (len(url) > 0):
			link = "youtube-dl -f bestaudio -o outfile " + url
			print "Downloading file at ", link
			# os.system(link)
			link = link.split(' ')
			
			# removing any previously available file
			somelist = os.listdir(os.getcwd())
			filename = [x for x in somelist if "outfile" in x]
			for f in filename:
				os.remove(f)
		
			# creating process for youtube-dl
			subprocess.call(link)
			os.rename('outfile', 'outfile.part')
		
			file.close()
			file = open("myfile", "w+")
			
			print "iteration completed"
			
			del link
			del somelist
			del filename
		file.close()
		del file
except KeyboardInterrupt:
		#observer.stop()
		exit(0)

observer.join()
