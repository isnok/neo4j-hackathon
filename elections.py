#!/usr/bin/env python3
""" scrape_elections.py - Scrape elections from deputies.xml

Usage:
    q_and_a.py [FILE]
"""

import bs4
import requests
from docopt import docopt

args = docopt(__doc__)
#print(args)

session = requests.Session()

def prep_url(url):
    if not 'abstimmungsverhalten' in url and url.endswith('.html'):
        return url[:-4] + '---abstimmungsverhalten-all.html#parlamentarische_arbeit'
    else:
        print('error!:', url)
        return url


def get_elections(url):
    rsp = session.get(url)
    rsp = session.get(prep_url(rsp.url))
    rsp.encoding = 'utf-8'
    #print(rsp.encoding)
    soup = bs4.BeautifulSoup(rsp.text)
    print(soup.title)
    elections = soup.findAll('div', attrs={'class':'abstimmungsverhalten box_margin'})
    if elections:
        elections = elections[0]
    else:
        return []
    result = []
    for elec in elections.findAll('div', attrs={'class': 'clearfix entry'}):
        result.append([ x.text for x in elec.findAll('div') ])
    return result

with open(args.get('FILE') or 'deputies.xml', 'r') as infile:
    soup = bs4.BeautifulSoup(infile.read())
    for p in soup.findAll('profile'):
        outfile = open('elections/' + p.uuid.text + '.csv', 'w')
        heading = 'uuid,date,title,vote\n'
        outfile.write(heading)
        #print(p.uuid.text)
        #print(p.url_profile.text)
        results = get_elections(p.url_profile.text)
        for r in results:
            date, title, vote = r
            line = '%s,%s,"%s","%s"\n' % (p.uuid.text, date, title, vote)
            outfile.write(line)
            #print(line)
