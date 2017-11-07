# -*- coding: utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup
from phpdoc.utils import get_query_url

#loading
import itertools
import threading
import time
import sys


done = False


def run():
    if len(sys.argv) == 1:
        quit()

    query = sys.argv[1]
     
    t = threading.Thread(target=loading)
    t.daemon = True
    t.start()
    
    url = get_query_url(query)
    resp = requests.get(url)

    if resp.status_code != 200:
        print('\nCould not find documentation for specified query')

    done = True
    
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    if not soup:
        return False

    synop = soup.find('div', {'class': 'methodsynopsis'})

    if not synop:
        return False
    
    synop_text = synop.text.replace('\n', '').replace('\r', '')

    print('\n' + synop_text)

def loading():
    try:
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rPlease Wait ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.flush()
    except KeyboardInterrupt:
        quit()
