#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

name = "MAXLAB"
country = "Sweden"
acronym = 'MAX'
isocode = 'SE'

MAXURL = "http://mobil.maxlab.lu.se/data/live_ring_status.xml"


def get_current():
    r = requests.get(MAXURL)

    soup = BeautifulSoup(r.text)

    currents = soup.findAll('current')

    return float(currents[2].contents[0])

if __name__ == '__main__':
    print get_current()
