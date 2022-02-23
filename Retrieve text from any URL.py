import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# just putting in a divider line for separation
# print('-------------------------------------------------------------------------------------------------------------')
#
# finding all the hrefs
# print(soup.find_all('href'))
#
# print('------------------------------------------------------------------------------------------------------------')
#
# Finding all the anchor tags
# print(soup.find_all('a'))
#
# print('------------------------------------------------------------------------------------------------------------')
#
# Finding all the paragraphs
# print(soup.find_all('p'))
#
# print('------------------------------------------------------------------------------------------------------------')

data = ''                         # This 3 lines below, will pull out the text from any web page
for data in soup.find_all('p'):   # and print it.
    print(data.get_text())
