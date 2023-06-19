# Exercise 1: Change your socket program so that it counts the number of characters 
# it has received and stops displaying any text after it has shown 3000 characters. 
# The program should retrieve the entire document and count the total number of characters 
# and display the count of the number of characters at the end of the document.

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
    quit()
#TODO : use dynamic url
cmd = 'GET http://data.pr4e.org/intro.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

count = 0
received = b""

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    # count = count + len(data)
    # print('count', count)
    # print(data.decode(),end='')
    received = received + data
    

mysock.close()
# print('Data:', received)

pos = received.find(b'\r\n\r\n')
actualData = received[pos+4:].decode()
# print('only data::::', actualData.decode())

charLen = 0

for characters in actualData:
    charLen = charLen + 1
    if charLen == 3000:
        break
    print(characters)
    
print('total character count:', charLen)




# Code: http://www.py4e.com/code3/socket1.py
