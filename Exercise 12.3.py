# Use urllib to replicate the previous exercise of (12.1):-
#
# import socket
#
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
# retrieving the document from a URL, (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document. Don’t
# worry about the headers for this exercise, simply show the first 3000
# characters of the document contents.

# use this url: http://data.pr4e.org/romeo.txt to test the program



import urllib.request, urllib.parse , urllib.error

count = 0
url = input('url: ')
fhand = urllib.request.urlopen(url)
word = fhand.read(3000).decode()
print(word)
for letter in word:
    count = count + 1                    # this line will count spaces/newlines
    print(letter, count)

# the code below will not count newlines/spaces
    # if letter.isalnum():
    #     count = count + 1
    #     print(letter, count)
