# Extracting Data from JSON
#
# In this assignment you will write a Python program somewhat similar to
#
# http://www.py4e.com/code3/json2.py.
#
# The program will prompt for a URL, read the JSON data from that URL using urllib
# and then parse and extract the comment counts from the JSON data,
# compute the sum of the numbers in the file and enter the sum below:
#
# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing
# and the other is the actual data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#
# Actual data: http://py4e-data.dr-chuck.net/comments_867382.json (Sum ends with 93)
#
# You do not need to save these files to your folder
# since your program will read the data directly from the URL.
# Note: Each student will have a distinct data url for the assignment -
# so only use your own data url for analysis.
# The data consists of a number of names and comment counts in JSON as follows:
#
#     {
#         comments: [
#             {
#                 name: "Matthias"
#                 count: 97
#             },
#             {
#                 name: "Geomer"
#                 count: 97
#             }
#                 ...
#         ]
#     }
#
# The closest sample code that shows how to parse JSON and extract a list is
#
# json2.py.
#
# You might also want to look at geoxml.py to see how to prompt
# for a URL and retrieve data from a URL

import urllib.request, urllib.error, urllib.parse
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0

url = input('Enter url: ')
html = urllib.request.urlopen(url, context=ctx).read().decode()
# print(html)
# print("=====================================================")
info = json.loads(html)
# print(info)
# print('======================================================')
#print(info['comments'])

for items in info['comments']:
    x = items['count']
    sum = sum + x

print(sum)



# print(info['comments']["name"])