#!/usr/bin/python
'''
Return the current at Pohang
'''

import urllib

name = "Pohang Accelerator Laboratory"
country = "Pohang, South Korea"
acronym = 'POHANG'
isocode = 'KR-47'

POHANG_URL = 'http://141.223.48.196/gnuplot/beam_daily_view.html?pvNamef=G:BEAMCURRENT'

offset = '::-15'
def get_current():
	A = urllib.urlopen(POHANG_URL).readlines()

	I = A[36].rstrip().rstrip('</b></font><font size=4><b>mA</b></font>').lstrip('<font color=red size=4><b>')
 
	return eval(I)
	
if __name__ == '__main__':
	print get_current()
