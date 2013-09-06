#!/usr/bin/python
'''
Return the current at SLS
'''

import re

import requests
from bs4 import BeautifulSoup

name = "Stanford Synchrotron Radiation Lightsource"
country = "Menlo Park, USA"
acronym = 'SSRL'
isocode = 'US-CA'

SSRL_URL = 'http://www-ssrl.slac.stanford.edu/talk_display.html'


def get_current():
    r = requests.get(SSRL_URL)
    soup = BeautifulSoup(r.text)

    # gives Beam Current: XX mA
    webtxt = soup.findAll('td', {'class': 'left'})[0].contents[4].strip()

    current_txt = re.search(r"[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?", webtxt)

    return float(current_txt.group(0))

if __name__ == '__main__':
    print get_current()
