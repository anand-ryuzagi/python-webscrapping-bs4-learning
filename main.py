import requests
import html5lib
from bs4 import BeautifulSoup

#step1 -get the html
url = "http://codewithharry.com"
req = requests.get(url)
htmlcontent = req.content
# print(htmlcontent)

#step2- parse the html
soup = BeautifulSoup(htmlcontent,'html.parser')
# print(soup.prettify)

#step3- html tree transversal

#commonly used types of object:
#1.tag   print(type(title))
#2.Navigablestring  print(type(title.string))
#3.BeautifulSoup print(type(soup))
#4.comment
# get comments
# markup = "<p><!-- this is a comment></p>"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))

# Get the title of html page 
title = soup.title

#get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)

# get all the anchors tags from the page
anchors = soup.find_all('a')
# print(anchors)

#get the single paragraph
para1 = soup.find('p')

# get the classes of a tags
class1 = soup.find('p')['class']

#find all the elements with class lead
lead1 = soup.find_all('p',class_='lead')

#get the text from the tags
text1 = soup.find('p').get_text()

#get all the links on the page
anchors = soup.find_all('a')
for link in anchors:
    print(link.get('href'))

#get links with no repeat
all_links = set()
for link in anchors:
    if( link.get('href') != '#'):    
        all_links.add(link.get('href'))


# .contents = a tag children are available in the list
# .children = a tag children in the generator, used for big website


# get div by id and contents
# navbarsupport = soup.find(id='')
# for el in navbarsupport.contents:
#   print(el)
# for el in navbarsupport.children:
#   print(el)

# #see the striper_string
# for item in navbarsupport.striper_string:
#     print(item)

# see the parents 
# for item in navbarsupport.parents:
#     print(item.name)

# to see the next lines
# navbarsupport.next_sibling

# css selector 
# elements = soup.select('#id')
# print(elements)