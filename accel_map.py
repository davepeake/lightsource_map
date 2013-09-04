#!/usr/bin/python
'''
Script which calls other scripts to scrape status pages to retrieve stored current.

Generates a google chart map 
'''

import os
from pygooglechart import MapChart

# accelerators supported
import asp, sls, als, diamond, nsls, esrf, spring8, ssrl, pf, elettra, anka, astrid, pohang

problems = '''
Current problems:
<ul>
<li> APS: Italicised text means that tesseract can't OCR it. Need to de-skew text.
<li> CLS: Crazy star-trek status page is trouble. Probably just needs some special attention to work.
<li> MAXLAB: Uses a java applet, so requires rendering in a browser before information is given up.
<li> ALBA: Isn't working yet, this is just here to remind me
<li> SOLEIL: Could work but they're in machine down mode at the moment so their status page isn't working.
<li> DESY: Looks promising but their status pages are broken at the moment.
<li> TPS: Another java applet
</ul>
'''

class Accelerator:
	def __init__(self, mod=None, name='', country='',isocode='',offset='',priority=0):
		# mod can have the name and country in it
		# the name isn't defined then use that one
		if name == '' and ('name' in dir(mod)):
			self.name = mod.name
		else:
			self.name = name

		self.acronym = mod.acronym
	
		if offset == '' and ('offset' in dir(mod)):
			self.offset = mod.offset
		else:
			self.offset = offset			
	
		if offset == 0 and ('priority' in dir(mod)):
			self.priority = mod.priority
		else:
			self.priority = priority

		if country == '' and ('country' in dir(mod)):			
			self.country = mod.country
		else:
			self.country = country

		if country == '' and ('isocode' in dir(mod)):
			self.isocode = mod.isocode
		else:
			self.isocode = isocode
		
		self.mod = mod
		# check that mod has a get_current function
		if 'get_current' not in dir(self.mod):
			self.mod = None

	def get_current(self):
		if self.mod == None:
			return -1
		else:
			try:
				I = self.mod.get_current()
			except:
				I = -1
			return I

if __name__ == '__main__':
	acc = [Accelerator(mod=asp), Accelerator(mod=sls), Accelerator(mod=diamond), Accelerator(mod=nsls), \
		Accelerator(mod=esrf), Accelerator(mod=ssrl), Accelerator(mod=spring8), Accelerator(mod=als), \
		Accelerator(mod=elettra), Accelerator(mod=anka), Accelerator(mod=astrid), Accelerator(mod=pohang), \
		Accelerator(mod=pf)]

	chart = MapChart(600,350)

	data_dict = {}
	counter=0
	for a in acc:
		#I = 100 + counter;
		#counter += 1
		I = a.get_current()
		a.I = I
		data_dict[a.isocode] = I

		print a.acronym, I, type(I)

	#url = http://chart.apis.google.com/chart?cht=map&cht=map:fixed=-60,-20,80,-35&chs=600x350&chd=s:9PfAu&chld=US-NY|CH|US-CA|AU-VIC|GB
	#chart.add_data_dict(data_dict)

	chart.add_data(data_dict.values())
	chart.set_codes(data_dict.keys())
	chart.zoom = '-60,-20,80,-35'

	counter = 0	
	for k in data_dict.keys():	
		for a in acc:
			if a.isocode == k:
				name = 'f%s:+%2.1f'%(a.acronym,a.I)

				if a.offset:
					chart.add_marker(0,counter,name,'000000',10,a.priority,a.offset)
				else:
					chart.add_marker(0,counter,name,'000000',10,a.priority)
						
				counter = counter + 1
				break	

	# european chart
	#chart.add_marker(0,1,'fTest+2','000000',10)
	c1 = chart.get_url()

	chart.zoom = '30,-10,60,45'

	c2 = chart.get_url()

	fout = open('index.html','w')

	fout.write('<HEAD><meta http-equiv="refresh" content="300"><BODY><center><img src="%s" border=1 /><p><img src="%s" border=1 /></center><p>%s</BODY></HEAD>'%(c1,c2,problems))

	fout.close()
