import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter url: ') # Enter http://www.dr-chuck.com/page1.html
html = urllib.request.urlopen(url).read() # the urllib opens the page as a file
                                         # and the .read() reads the entire thing into the variable html.
                                         # Th this point, all the python documenation methods will work on it
soup = BeautifulSoup(html, 'html.parser')

# the line below retrieves all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

# RESULT :-
# http://www.dr-chuck.com/page2.htm


# An anchor tag, or anchor link,
# is a web page element that links to another location on the same page.
# They are typically used for long or text-heavy pages
# so that visitors can jump to a specific part of the page without having to scroll as much.
#
# Since clicking on an anchor link takes visitors where they want to go without much effort,
# they improve the overall user experience, which aids in the conversion process.
# Not only do they make it fast and easy for visitors to navigate your page,
# but they can serve as visual cues,
# pointing people toward elements that are integral to your conversion goal.
# It’s worth mentioning that they can be static or animated.
#
# When animated, anchor tags have the potential to attract more attention
# because it’s likely the only thing moving on the page.
# And when you combine animation with white space,
# you get a powerful combination that draws people’s attention where you want it.
# In the anchor tag examples below,
# you’ll notice this design technique can be used in a variety of ways.