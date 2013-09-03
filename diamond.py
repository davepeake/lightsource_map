#!/usr/bin/python
'''
Return the current at Diamond
'''

import urllib

name = "Diamond"
country = "England"
acronym = 'DLS'
isocode = 'GB-OXF'

DIAMOND_URL = "http://controls.diamond.ac.uk/webstatus/index.php"

def get_current():
	A = urllib.urlopen(DIAMOND_URL).readlines()
	#A = open('images/index.php').readlines()

	I = eval(A[39].rstrip())

	return I

if __name__ == '__main__':
	print get_current()
