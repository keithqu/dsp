"""
Analysis of Gas Prices in the Greater Toronto Area
Stages:
1. Get addresses of gas stations from yellowpages.ca, remove stations with no address or incomplete addresses.
2. Use geopy and the GoogleV3 engine to find the coordinates of each address.
3. Search google maps to get the all available prices (diesel, regular, premium, etc.) for all gas stations

4+. and more...
"""

from bs4 import BeautifulSoup
import urllib
import re
import pandas as pd
import numpy as np
import datetime
import sys
import time
import json
from geopy.geocoders import GoogleV3
import seaborn as sns
from time import sleep
geolocator = GoogleV3()
%matplotlib inline
today = datetime.datetime.now()

# Get the names and addressess of gas stations listed in Yellow Pages in the Toronto region

def get_addresses (page_num):
    with open('gas_dict.json', 'r') as infile:
        gas_dict = json.load(infile)
        
    url = 'https://www.yellowpages.ca/search/si/'+str(page_num)+'/Gas%20Stations/Toronto+ON'
    try:
        html = urllib.request.urlopen(url).read()
    except:
        return page_num
    soup = BeautifulSoup(html, 'html.parser')
        
    content = soup.findAll('div',{'class':'listing__content__wrap'})

    for n in range(len(content)):
        try:
            name = content[n].findAll('a')[0].get('title').split('-')[0]
        except:
            name = '#NO NAME'
        
        try:
            addr_ele = content[n].findAll('span',{'class':'listing__address--full'})[0].findAll('span')
            addr = ','.join([addr_ele[i].string for i,e in enumerate(addr_ele)])
        except:
            addr = '#NO ADDRESS#'
        
        gas_dict[addr] = {'name':name}
 
    with open('gas_dict.json', 'w') as outfile:
        json.dump(gas_dict,outfile)
    
    return page_num + 1

def address_main():
    # If file doesn't exist, create it
    try:
        with open('gas_dict.json', 'r') as infile:
            gas_dict = json.load(infile)
    except:
        with open('gas_dict.json', 'w') as outfile:
            gas_dict={}
            json.dump(gas_dict,outfile)
    
    page_num = 20
    while page_num < 22:
        print('Fetching page ',page_num)
        page_num = get_addresses(page_num)
        sleep(np.random.random(1)*2+2)


def clean_addresses():
    with open('gas_dict.json', 'r') as infile:
        gas_dict = json.load(infile)
    
    gas_dict.pop('#NO ADDRESS#',None)
    gas_dict.pop('ON',None)
    
    with open('gas_dict.json', 'w') as outfile:
        json.dump(gas_dict,outfile)
