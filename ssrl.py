#!/usr/bin/python
'''
Return the current at SLS
'''

import urllib

name = "Stanford Synchrotron Radiation Lightsource"
country = "Menlo Park, USA"
acronym = 'SSRL'
isocode = 'US-CA'

SSRL_URL = 'http://www-ssrl.slac.stanford.edu/talk_display.html'

def get_current():
	A = urllib.urlopen(SSRL_URL).readlines()

	I = A[138].rstrip().rstrip(' mA</td>').lstrip('  <td class="right">Beam Current: ').lstrip()
 
	return eval(I)
	
if __name__ == '__main__':
	print get_current()
