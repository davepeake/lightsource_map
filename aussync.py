#!/usr/bin/python
# TODO: Position

import urllib

def remove_tags(s):
	st = s.find('<')
	en = s.find('>')

	if st == -1 or en == -1:
		return s
	else:
		return s.replace(s[st:en+1],'')

class CSynchData:
	def __init__(self, url='https://vbl.synchrotron.org.au/fsm/index.wml'):
		self.url = url

		self.data = {}

		self.ParseData()

	def ParseData(self):
		buff = urllib.urlopen(self.url)

		for line in buff:
			if len(line.split()) == 0:
				continue
			# parse for information
			linetype = line.split()[0]
			linesplit = line.split()
			if linetype == '<p>' or linetype == '</p>' or linetype == '<card' or linetype == '</card>' or linetype == '</wml>':
				continue
			elif linetype == 'Beam':
				if linesplit[1] == 'Current:':
					self.data['current'] = linesplit[2] 
				elif linesplit[1] == 'Lifetime:':
					self.data['lifetime'] = linesplit[2]
			elif linetype == 'Current':
				self.data['currentxlifetime'] = linesplit[3]
			elif linetype == 'Integrated':
				self.data['integrated'] = linesplit[2]
			elif linetype == 'PSS':
				self.data['mastershutter'] = remove_tags(" ".join(linesplit[4:]))
			elif linetype == 'Infra':
				self.data['IR'] = remove_tags(" ".join(linesplit[2:]))
			elif linetype == 'Micro':
				self.data['MX2'] = remove_tags(" ".join(linesplit[2:]))
			elif linetype == 'Macromolecular':
				self.data['MX1'] = remove_tags(" ".join(linesplit[2:]))
			elif linetype == 'Medical':
				self.data['IMT'] = remove_tags(" ".join(linesplit[2:]))
			elif linetype == 'Microspectroscopy:':
				self.data['XFM'] = remove_tags(" ".join(linesplit[1:]))
			elif linetype == 'Powder':
				self.data['PX'] = remove_tags(" ".join(linesplit[2:]))
			elif linetype == 'Status:':
				self.data['status'] = remove_tags(" ".join(linesplit[1:]))
			elif linetype == 'X-ray':
				self.data['XAS'] = remove_tags(" ".join(linesplit[3:]))
			elif linetype == 'Small/Wide':
				self.data['SAXWAX'] = remove_tags(" ".join(linesplit[3:]))
			elif linetype == 'Soft':
				self.data['SX'] = remove_tags(" ".join(linesplit[2:]))
			else:
				pass
				#print "Unknown linetype:", linetype
	
	def parse_beamline_status(self,s):
		if s == 'No Alarm':
			return 1
		else:
			return 0	

	def print_data(self):
		if len(self.data.keys()) == 0:
			return

		print 'Beam Current:', self.data['current'], 'mA'
		print 'Beam Lifetime:', self.data['lifetime'], 'Hrs'
		print 'Current x Lifetime:', self.data['currentxlifetime'], 'AHrs'
		print 'Integrated Current:', self.data['integrated'], 'AHrs'
		print '-===============-'
		print ' Beamline Status '
		print '-===============-'
		print 'Master Shutter:', self.parse_beamline_status(self.data['mastershutter'])
		print 'PX:\t', self.parse_beamline_status(self.data['PX'])
		print 'XAS:\t', self.parse_beamline_status(self.data['XAS'])
		print 'SAXWAX:\t', self.parse_beamline_status(self.data['SAXWAX'])
		print 'SX:\t', self.parse_beamline_status(self.data['SX'])
		print 'XFM:\t', self.parse_beamline_status(self.data['XFM'])
		print 'IMT:\t', self.parse_beamline_status(self.data['IMT'])
		print 'IR:\t', self.parse_beamline_status(self.data['IMT'])


if __name__ == "__main__":
	cs = CSynchData()

	cs.print_data()

