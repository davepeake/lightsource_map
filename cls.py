#!/usr/bin/python
'''
Return the current at CLS
'''

import urllib, os
from PIL import Image, ImageFile

name = "Canadian Light Source"
country = "Saskatoon, Canada"
acronym = 'CLS'
isocode = 'CA-SK'

CLS_URL = 'ftp://transfer.lightsource.ca/BuildingStatus/ringstat.jpg'

def get_current():
	gif = urllib.urlopen(CLS_URL)
	#gif = 'images/nsls_ringstat.gif'

	parser = ImageFile.Parser()
	while True:
		s = gif.read(1024)
		if not s:
			break
		parser.feed(s)

	A = parser.close()	
	A.show()
	#A = PIL.Image.open(gif)
	B = A.crop([306,174,361,201])

	B.save('temp.tif')
	B.show()

	os.popen('tesseract temp.tif temp 2> /dev/null')

	#check if temp.txt exists	
	I = eval(open('temp.txt').readline().rstrip())

	os.system('rm temp.tif temp.txt')

	return I

if __name__ == '__main__':
	print get_current()
