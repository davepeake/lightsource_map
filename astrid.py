#!/usr/bin/python
'''
Return the current at ALS 
'''

import urllib

name = "ASTRID"
country = "Arhus, Denmark"
acronym = 'ASTRID'
isocode = 'DK-82'

ASTRID_URL = 'http://www.isa.au.dk/status/plots/isaAstridelstatus.asp'

def get_current():
	A = urllib.urlopen(ASTRID_URL).readlines()

	I = A[103].rstrip().rstrip('</td>')

	return eval(I)

if __name__ == '__main__':
	print get_current()
