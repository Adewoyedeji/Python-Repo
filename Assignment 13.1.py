# Extracting Data from XML
#
# In this assignment you will write a Python program somewhat similar to
# http://www.py4e.com/code3/geoxml.py.
# The program will prompt for a URL, read the XML data from that URL using urllib
# and then parse and extract the comment counts from the XML data,
# compute the sum of the numbers in the file.
#
# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing
# and the other is the actual data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#
# Actual data: http://py4e-data.dr-chuck.net/comments_867381.xml (Sum ends with 41)
#
# You do not need to save these files to your folder
# since your program will read the data directly from the URL.
# Note: Each student will have a distinct data url for the assignment -
# so only use your own data url for analysis.
#
# Data Format and Approach
#
# The data consists of a number of names and comment counts in XML as follows:
#
# <comment>
#   <name>Matthias</name>
#   <count>97</count>
# </comment>
#
# You are to look through all the <comment> tags
# and find the <count> values sum the numbers.
# The closest sample code that shows how to parse XML is geoxml.py.
# But since the nesting of the elements in our data
# is different than the data we are parsing in that sample code
# you will have to make real changes to the code.
# To make the code a little simpler,
# you can use an XPath selector string to look through the entire tree of XML
# for any tag named 'count' with the following line of code:
#
# counts = tree.findall('.//count')

# Take a look at the Python ElementTree documentation
# and look for the supported XPath syntax for details.
# You could also work from the top of the XML down to the comments node
# and then loop through the child nodes of the comments node.
#
# Sample Execution
#
# $ python3 solution.py
# Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
# Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
# Retrieved 4189 characters
# Count: 50
# Sum: 2...

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0

url = input('Enter url: ')
html = urllib.request.urlopen(url, context=ctx).read().decode()
#print(html)
stuff = ET.fromstring(html)
lst = stuff.findall('comments/comment')
#print(stuff)
#print(lst)
for item in lst:
  num = int(item.find('count').text) # This line converts the str number to integer for addition.
  #print(num)
  sum = sum + num
print(sum)

# The XML from  http://py4e-data.dr-chuck.net/comments_42.xml  is below
#
# <commentinfo>
# <note>This file contains the sample data for testing</note>
# <comments>
# <comment>
# <name>Romina</name>
# <count>97</count>
# </comment>
# <comment>
# <name>Laurie</name>
# <count>97</count>
# </comment>
# <comment>
# <name>Bayli</name>
# <count>90</count>
# </comment>
# <comment>
# <name>Siyona</name>
# <count>90</count>
# </comment>
# <comment>
# <name>Taisha</name>
# <count>88</count>
# </comment>
# <comment>
# <name>Alanda</name>
# <count>87</count>
# </comment>
# <comment>
# <name>Ameelia</name>
# <count>87</count>
# </comment>
# <comment>
# <name>Prasheeta</name>
# <count>80</count>
# </comment>
# <comment>
# <name>Asif</name>
# <count>79</count>
# </comment>
# <comment>
# <name>Risa</name>
# <count>79</count>
# </comment>
# <comment>
# <name>Zi</name>
# <count>78</count>
# </comment>
# <comment>
# <name>Danyil</name>
# <count>76</count>
# </comment>
# <comment>
# <name>Ediomi</name>
# <count>76</count>
# </comment>
# <comment>
# <name>Barry</name>
# <count>72</count>
# </comment>
# <comment>
# <name>Lance</name>
# <count>72</count>
# </comment>
# <comment>
# <name>Hattie</name>
# <count>66</count>
# </comment>
# <comment>
# <name>Mathu</name>
# <count>66</count>
# </comment>
# <comment>
# <name>Bowie</name>
# <count>65</count>
# </comment>
# <comment>
# <name>Samara</name>
# <count>65</count>
# </comment>
# <comment>
# <name>Uchenna</name>
# <count>64</count>
# </comment>
# <comment>
# <name>Shauni</name>
# <count>61</count>
# </comment>
# <comment>
# <name>Georgia</name>
# <count>61</count>
# </comment>
# <comment>
# <name>Rivan</name>
# <count>59</count>
# </comment>
# <comment>
# <name>Kenan</name>
# <count>58</count>
# </comment>
# <comment>
# <name>Hassan</name>
# <count>57</count>
# </comment>
# <comment>
# <name>Isma</name>
# <count>57</count>
# </comment>
# <comment>
# <name>Samanthalee</name>
# <count>54</count>
# </comment>
# <comment>
# <name>Alexa</name>
# <count>51</count>
# </comment>
# <comment>
# <name>Caine</name>
# <count>49</count>
# </comment>
# <comment>
# <name>Grady</name>
# <count>47</count>
# </comment>
# <comment>
# <name>Anne</name>
# <count>40</count>
# </comment>
# <comment>
# <name>Rihan</name>
# <count>38</count>
# </comment>
# <comment>
# <name>Alexei</name>
# <count>37</count>
# </comment>
# <comment>
# <name>Indie</name>
# <count>36</count>
# </comment>
# <comment>
# <name>Rhuairidh</name>
# <count>36</count>
# </comment>
# <comment>
# <name>Annoushka</name>
# <count>32</count>
# </comment>
# <comment>
# <name>Kenzi</name>
# <count>25</count>
# </comment>
# <comment>
# <name>Shahd</name>
# <count>24</count>
# </comment>
# <comment>
# <name>Irvine</name>
# <count>22</count>
# </comment>
# <comment>
# <name>Carys</name>
# <count>21</count>
# </comment>
# <comment>
# <name>Skye</name>
# <count>19</count>
# </comment>
# <comment>
# <name>Atiya</name>
# <count>18</count>
# </comment>
# <comment>
# <name>Rohan</name>
# <count>18</count>
# </comment>
# <comment>
# <name>Nuala</name>
# <count>14</count>
# </comment>
# <comment>
# <name>Maram</name>
# <count>12</count>
# </comment>
# <comment>
# <name>Carlo</name>
# <count>12</count>
# </comment>
# <comment>
# <name>Japleen</name>
# <count>9</count>
# </comment>
# <comment>
# <name>Breeanna</name>
# <count>7</count>
# </comment>
# <comment>
# <name>Zaaine</name>
# <count>3</count>
# </comment>
# <comment>
# <name>Inika</name>
# <count>2</count>
# </comment>

# </comments>
# </commentinfo>