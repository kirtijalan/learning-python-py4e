# Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page. 
# You can use split('/') to break the URL into its component parts so you can extract the host name for the 
# socket connect call. Add error checking using try and except to handle the condition where the user enters 
# an improperly formatted or non-existent URL.

import socket

urlName = input('Enter a URL:')
hostName = urlName.split('/')[2]
print(hostName)
# try:

# except
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((hostName, 80))
    

except:
    print('URL is not of correct format.')
    
#TODO : use dynamic url
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()


# Code: http://www.py4e.com/code3/socket1.py
