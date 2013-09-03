#!/usr/bin/python
'''
Return the current at Spring-8
'''

import urllib

name = "Spring-8"
country = "Hyogo, Japan"
acronym = 'SPRING8'
isocode = 'JP-28'

SPRING8_URL = 'http://www.spring8.or.jp/ext/en/status/2.html'

priority = 1

def get_current():
	A = urllib.urlopen(SPRING8_URL).readlines()

	I = A[90].rstrip().rstrip('mA</FONT><BR></TD>').lstrip('<TD ALIGN=CENTER BGCOLOR="#B2C1FF"><FONT SIZE="+3">')

	try: 
		return eval(I)
	except:
		return 0
	
if __name__ == '__main__':
	print get_current()
