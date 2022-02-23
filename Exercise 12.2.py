# Change your socket1.py program
#
# import socket
# url = input('Enter url: ')
# urlbreak = url.split('/')
# host = urlbreak[2]
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# try:
#     mysock.connect((host, 80))
# except:
#     print('Bad url. Please enter new url')
#     quit()
# # the line below concatenates the strings in the bracket
# cmd = ('GET '+url+' HTTP/1.0\n\n').encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
#
# mysock.close()
#
# so that it counts the number
# of characters it has received and stops displaying any text after it has
# shown 3000 characters. The program should retrieve the entire docu-
# ment and count the total number of characters and display the count
# of the number of characters at the end of the document.

# use this url: http://data.pr4e.org/romeo.txt to test the program

import socket

count = 0
url = input('Enter url: ')
urlbreak = url.split('/')
host = urlbreak[2]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.connect((host, 80))
except:
    print('Bad url. Please enter new url')
    quit()

# the line below concatenates the strings in the bracket
cmd = ('GET '+url+' HTTP/1.0\n\n').encode()
mysock.send(cmd)

while True:
    if count == 3000:
        break
    data = mysock.recv(512)
    if len(data) < 1:
        break
    ddata = data.decode()
    for char in ddata:
        count = count + 1
    print(ddata)
print(count)


mysock.close()