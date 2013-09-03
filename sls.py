#!/usr/bin/python
'''
Return the current at SLS
'''

import urllib

name = "Swiss Light Source"
country = "Switzerland"
acronym = 'SLS'
isocode = 'CH-AG'

#SLS_URL = "http://sls.web.psi.ch/view.php/organization/status/realtime/index.html"
SLS_URL = 'http://abk.web.psi.ch/operation/kr/sls/sls_live.php'
def get_current():
	A = urllib.urlopen(SLS_URL).readlines()

	'''
	nextline = False
	for line in A:
		if nextline:
			s = line.find('>') + 1
			e = line[s:].find('<') + s
			return eval(line[s:e])
		if line.find('Beamcurrent') != -1:
			nextline = True
	'''
	line = A[11][1:]
	l = line.find('>')
	r = line.find('<')

	
	#print line[(l+1):r], l, r
	
	return float(line[(l+1):r])

if __name__ == '__main__':
	print get_current()
