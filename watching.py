import sys
import os
import subprocess
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
			                            datefmt='%Y-%m-%d %H:%M:%S')
						    
#	logging.basicConfig (level=logging,INFO,format="%(asctime)s - %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
	path = sys.argv[1] if len(sys.argv) > 1 else '.'
	event_handler = LoggingEventHandler()
	observer = Observer()
	observer.schedule(event_handler, path, recursive=True)
	observer.start()
	try :
		while True:
			time.sleep(1)
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
				subprocess.call(link)
				somelist = os.listdir(os.getcwd())
				filename = [x for x in somelist if "outfile" in x] [0]
				if ".part" not in filename:
					os.rename(filename, filename+'.part')
				print "iteration completed"
				temp.close()
				temp = open("status", "w+")
				temp.close()
			file.close()
	except KeyboardInterrupt:
			observer.stop()
	
	observer.join()
