# Scraping Numbers from HTML using BeautifulSoup.
#
# In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py.
# The program will use urllib to read the HTML from the data files below,
# and parse the data, extracting numbers and compute the sum of the numbers in the file.
#
# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing
# and the other is the actual data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#
# Actual data: http://py4e-data.dr-chuck.net/comments_867379.html (Sum ends with 35)
#
# You do not need to save these files to your folder since your program will read the data directly from the URL.
# Note: Each student will have a distinct data url for the assignment -
# so only use your own data url for analysis.
#
# Data Format
# The file is a table of names and comment counts.
# You can ignore most of the data in the file except for lines like the following:
#
# <tr><td>Modu</td><td><span class="comments">90</span></td></tr>
# <tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
# <tr><td>Hubert</td><td><span class="comments">87</span></td></tr>
# You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
#
# Look at the sample code provided.
# It shows how to find all of a certain kind of tag,
# loop through the tags and extract the various aspects of the tags.
#
# ...
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#    # Look at the parts of a tag
#    print 'TAG:',tag
#    print 'URL:',tag.get('href', None)
#    print 'Contents:',tag.contents[0]
#    print 'Attrs:',tag.attrs
#
# You need to adjust this code to look for span tags
# and pull out the text content of the span tag,
# convert them to integers and add them up to complete the assignment.
# Sample Execution
#
# $ python3 solution.py
# Enter - http://py4e-data.dr-chuck.net/comments_42.html
# Count 50
# Sum 2...

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors. These 3 lines below will always be the same to check for errors.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0
count = 0

url = input('Enter url: ')   # Enter http://py4e-data.dr-chuck.net/comments_42.html
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
#print(soup)

tags = soup('span')
#print(tags)
for tag in tags:
    x = int(tag.contents[0])
    count = count + 1
    sum = sum + x
print(count)
print(sum)

   # Look at the parts of a tag
   # print ('TAG:',tag)
   # print ('URL:',tag.get('href', None))
   # print ('Contents:',tag.contents[0])
   # print ('Attrs:',tag.attrs)

# RESULT OF THE PRINT STATEMENTS FROM LINE 71 T0 74
# Enter url: http://py4e-data.dr-chuck.net/comments_42.html
# TAG: <span class="comments">97</span>
# URL: None
# Contents: 97
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">97</span>
# URL: None
# Contents: 97
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">90</span>
# URL: None
# Contents: 90
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">90</span>
# URL: None
# Contents: 90
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">88</span>
# URL: None
# Contents: 88
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">87</span>
# URL: None
# Contents: 87
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">87</span>
# URL: None
# Contents: 87
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">80</span>
# URL: None
# Contents: 80
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">79</span>
# URL: None
# Contents: 79
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">79</span>
# URL: None
# Contents: 79
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">78</span>
# URL: None
# Contents: 78
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">76</span>
# URL: None
# Contents: 76
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">76</span>
# URL: None
# Contents: 76
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">72</span>
# URL: None
# Contents: 72
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">72</span>
# URL: None
# Contents: 72
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">66</span>
# URL: None
# Contents: 66
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">66</span>
# URL: None
# Contents: 66
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">65</span>
# URL: None
# Contents: 65
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">65</span>
# URL: None
# Contents: 65
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">64</span>
# URL: None
# Contents: 64
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">61</span>
# URL: None
# Contents: 61
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">61</span>
# URL: None
# Contents: 61
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">59</span>
# URL: None
# Contents: 59
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">58</span>
# URL: None
# Contents: 58
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">57</span>
# URL: None
# Contents: 57
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">57</span>
# URL: None
# Contents: 57
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">54</span>
# URL: None
# Contents: 54
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">51</span>
# URL: None
# Contents: 51
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">49</span>
# URL: None
# Contents: 49
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">47</span>
# URL: None
# Contents: 47
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">40</span>
# URL: None
# Contents: 40
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">38</span>
# URL: None
# Contents: 38
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">37</span>
# URL: None
# Contents: 37
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">36</span>
# URL: None
# Contents: 36
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">36</span>
# URL: None
# Contents: 36
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">32</span>
# URL: None
# Contents: 32
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">25</span>
# URL: None
# Contents: 25
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">24</span>
# URL: None
# Contents: 24
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">22</span>
# URL: None
# Contents: 22
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">21</span>
# URL: None
# Contents: 21
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">19</span>
# URL: None
# Contents: 19
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">18</span>
# URL: None
# Contents: 18
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">18</span>
# URL: None
# Contents: 18
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">14</span>
# URL: None
# Contents: 14
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">12</span>
# URL: None
# Contents: 12
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">12</span>
# URL: None
# Contents: 12
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">9</span>
# URL: None
# Contents: 9
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">7</span>
# URL: None
# Contents: 7
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">3</span>
# URL: None
# Contents: 3
# Attrs: {'class': ['comments']}
# TAG: <span class="comments">2</span>
# URL: None
# Contents: 2
# Attrs: {'class': ['comments']}
#
# Process finished with exit code 0

