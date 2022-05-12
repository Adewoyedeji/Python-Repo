# The program will use urllib to read the HTML from the data files below,
# extract the href= values from the anchor tags,
# scan for a tag that is in a particular position relative to the first name in the list,
# follow that link and repeat the process a number of times and report the last name you find.

# Sample problem:
# Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1).
# Follow that link. Repeat this process 4 times.
# The answer is the last name that you retrieve.
#
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
n = 4
while True:
    if n < 1:
        break
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    # Retrieve all of the anchor tags
    tags = soup('a')          # A list of all the anchor tags.
    #print(tags)
    y = tags[2]               # The third anchor tag
    #print(y)
    x = y.get('href', None)   # This pulls out the url in the anchor tag
    #print(x)
    z = y.text                # This extracts the text inside an anchor tag.
    print(z)
    url = x
    n = n - 1





