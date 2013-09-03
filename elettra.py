#!/usr/bin/python
'''
Return the current at ALS 
'''

import urllib

name = "ELETTRA"
country = "Trieste, Italy"
acronym = 'ELETTRA'
isocode = 'IT-36'

ELETTRA_URL = 'http://www.elettra.trieste.it/accelerator/machine_status.php'

def get_current():
	A = urllib.urlopen(ELETTRA_URL).readlines()

	I = A[16].lstrip('<tr><td><strong>Current</strong></td><td>').rstrip().rstrip(' mA</td></tr>')

	return eval(I)

if __name__ == '__main__':
	print get_current()
