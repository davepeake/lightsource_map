#!/usr/bin/python
'''
Return the current at ESRF
'''

import urllib, os
from PIL import Image, ImageFile

name = "European Synchrotron Radiation Facility"
country = "Grenoble, France"
acronym = 'ESRF'
isocode = 'FR-V'

ESRF_URL = 'http://www.esrf.eu/esrf_status/gifs/img1.png'

def get_current():
	gif = urllib.urlopen(ESRF_URL)
	#gif = 'images/nsls_ringstat.gif'

	parser = ImageFile.Parser()
	while True:
		s = gif.read(1024)
		if not s:
			break
		parser.feed(s)

	A = parser.close()	
	#A = PIL.Image.open(gif)
	B = A.crop([5,27,120,62])

	B.save('temp.tif')

	os.popen('tesseract temp.tif temp 2> /dev/null')

	#check if temp.txt exists	
	I = eval(open('temp.txt').readline().split()[0].rstrip())

	os.system('rm temp.tif temp.txt')

	return I

if __name__ == '__main__':
	print get_current()
