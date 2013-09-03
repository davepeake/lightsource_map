#!/usr/bin/python
'''
Return the current at ALS 
'''

import urllib

name = "Advanced Light Source"
country = "Berkely"
acronym = 'ALS'
isocode = 'US-OR'

ALS_URL = "http://www-als.lbl.gov/als/als_ops/status.html"

#offset = '::10'

def get_current():
	A = urllib.urlopen(ALS_URL).readlines()

	I = eval( A[96].lstrip('<center><h1>').rstrip().rstrip(' mA</h1></center>') )

	return I

if __name__ == '__main__':
	print get_current()
