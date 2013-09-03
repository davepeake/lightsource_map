#!/usr/bin/python
'''
Return the current at APS
'''

import urllib, os
from PIL import Image, ImageFile
import numpy

name = "Advanced Photon Source"
country = "Chicago, USA"
acronym = 'APS'
isocode = 'US-IL'

APS_URL = 'http://www.aps.anl.gov/aod/blops/plots/smallStatusPlot.png'

offset = '::10'

def get_current():
	gif = urllib.urlopen(APS_URL)
	#gif = 'images/nsls_ringstat.gif'

	parser = ImageFile.Parser()
	while True:
		s = gif.read(1024)
		if not s:
			break
		parser.feed(s)

	A = parser.close()	
	#A = PIL.Image.open(gif)
	B = A.crop([187,18,240,38])

	Ba = numpy.asarray(B)


	B.save('temp.tif')
	B.show()

	os.popen('tesseract temp.tif temp 2> /dev/null')

	#check if temp.txt exists	
	I = eval(open('temp.txt').readline().rstrip())

	os.system('rm temp.tif temp.txt')

	return I

if __name__ == '__main__':
	print get_current()
