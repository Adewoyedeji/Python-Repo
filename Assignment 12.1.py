# Welcome ADEWOYE AYODEJI ADESHOLA from Using Python to Access Web Data
#
# Exploring the HyperText Transport Protocol
#
# You are to retrieve the following document using the HTTP protocol
# in a way that you can examine the HTTP Response headers.
#
# http://data.pr4e.org/intro-short.txt
#
# There are three ways that you might retrieve this web page
# and look at the response headers:
#
# Preferred: Modify the socket1.py program to retrieve the above URL
# and print out the headers and data.
# Make sure to change the code to retrieve the above URL -
# the values are different for each URL.
# Open the URL in a web browser with a developer console
# or FireBug and manually examine the headers that are returned.

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                     # This line doesn't actually make the connection.
                                     # This is more like a door way.
                                     # Think of this line like a file handle,
                                     # that doesn't have any data associated with it yet.
#
mysock.connect(('data.pr4e.org', 80))
                                     #This line connects our socket
                                     # to a destination across the internet
                                     # with a domain name "data,pr4e.org", using port 80
#
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n'.encode()
                                     # The GET all the way to HTTP/1.0 is the http rules
                                     # The first \n is 'end of line'
                                     # The second \n is 'blank line'
                                     # The ".encode()" is there because there are strings inside python
                                     # that are in unicode that needs to be sent out in UTF-8 bytes
#
mysock.send(cmd)                     # This line send the command 'cmd'

while True:
    data = mysock.recv(152)
    if len(data) < 1:   # This line denotes end of file since that is when its length will be less than 1
        break
    print(data.decode())
mysock.close()         # This closes the socket