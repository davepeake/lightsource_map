#!/usr/bin/python 
'''
Australian Synchrotron
'''

import aussync as AS

name = 'Australian Synchrotron'
country = 'Australia'
acronym = 'AS'
isocode = 'AU-VIC'

def get_current():
	cAS = AS.CSynchData()

	return eval(cAS.data['current'])

if __name__ == '__main__':
	print get_current()
