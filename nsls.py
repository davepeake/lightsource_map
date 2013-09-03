#!/usr/bin/python
'''
Return the current at NSLS
'''

import urllib, os
from PIL import Image, ImageFile

name = "National Synchrotron Light Source"
country = "Brookhaven, USA"
acronym = 'NSLS'
isocode = 'US-NY'

NSLS_URL = 'http://status.nsls.bnl.gov/Status/images/ringstat.gif'

def get_current():
	gif = urllib.urlopen(NSLS_URL)
	#gif = 'images/nsls_ringstat.gif'

	parser = ImageFile.Parser()
	while True:
		s = gif.read(1024)
		if not s:
			break
		parser.feed(s)

	A = parser.close()	
	#A = PIL.Image.open(gif)
	B = A.crop([54,75,163,109])

	B.save('temp.tif')
	
	os.popen('tesseract temp.tif temp 2> /dev/null')

	#check if temp.txt exists	
	I = eval(open('temp.txt').readline().split()[0].rstrip())

	os.system('rm temp.tif temp.txt')

	return I

if __name__ == '__main__':
	print get_current()
