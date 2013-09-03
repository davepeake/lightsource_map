#!/usr/bin/python
'''
Return the current at ALS 
'''

import urllib

name = "Angstroemequelle Karlsruhe"
country = "Karlsruhe, Germany"
acronym = 'ANKA'
isocode = 'DE-BW'

ANKA_URL = 'http://ankaweb.fzk.de/_popup/status.html'

def get_current():
	A = urllib.urlopen(ANKA_URL).readlines()

	I = A[29].lstrip().lstrip('<td>').rstrip().rstrip('</td>')

	return eval(I)

if __name__ == '__main__':
	print get_current()
