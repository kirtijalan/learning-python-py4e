import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter count:')
pos = input('Enter position:')

urlList = [url]


def currData(urlVal):
    html = urllib.request.urlopen(urlVal, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    totalPos = 0
    tags = soup('a')
    for tag in tags:
        totalPos = totalPos + 1
        if totalPos == int(pos):
            print('Retreiving:', tag.get('href', None))
            urlList.append(tag.get('href', None))

totalCount = 0

while totalCount < int(count):
    # print(urlList[totalCount])
    currData(urlList[totalCount])
    totalCount = totalCount + 1