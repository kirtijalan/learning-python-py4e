import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')

uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
tree = ET.fromstring(data)
total = 0
counts = tree.findall('.//count')
for each in counts:
    total = total + int(each.text)
    # print(int(each.text))
    
print(total)