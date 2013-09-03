#!/usr/bin/python
'''
Return the current at SLS
'''

import urllib

name = "Photon Factory"
country = "Tsukuba, Japan"
acronym = 'PF'
isocode = 'JP-08'

PF_URL = 'http://www-pfring.kek.jp/PF/status/text_status_html'

offset = '::10' 

def get_current():
	A = urllib.urlopen(PF_URL).readlines()

	I = A[5].split('=')[1].lstrip().split()[0]
 
	return eval(I)
	
if __name__ == '__main__':
	print get_current()
