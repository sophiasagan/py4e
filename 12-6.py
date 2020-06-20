# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
counter = 0
# Retrieve all of the anchor tags
while counter < 7:
    loop_url = tags[17].get('href',None)
    print('Retrieving: ',loop_url)
    html2 = urllib.request.urlopen(loop_url, context=ctx).read()
    soup2 = BeautifulSoup(html2, 'html.parser')
    tags = soup2('a')
    counter += 1
