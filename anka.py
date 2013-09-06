#!/usr/bin/python
'''
Return the current at ALS 
'''

import requests
from bs4 import BeautifulSoup

name = "Angstroemequelle Karlsruhe"
country = "Karlsruhe, Germany"
acronym = 'ANKA'
isocode = 'DE-BW'

ANKA_URL = 'http://ankastatserv.ka.fzk.de:8080/axis/StatusMedium'


def get_current():
    r = requests.get(ANKA_URL)

    soup = BeautifulSoup(r.text)

    qq = soup.find("b", {'id': 'current'})

    return float(qq.contents[0].split()[0])

if __name__ == '__main__':
    print get_current()
