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

total = 0
count = 0

#retrieve all span elements
spans = soup('span')
for span in spans:
    val = span.contents[0]
    if(int(val)) :
        count = count + 1
        total = total + int(val)
    
print('Count', count)
print('Sum', total)