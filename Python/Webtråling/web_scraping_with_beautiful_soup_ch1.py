#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 08:42:40 2020

@author: bwarland
"""

from urllib.request import urlopen
from urllib.error   import HTTPError 
from bs4            import BeautifulSoup
import re

html_1=urlopen("http://pythonscraping.com/pages/page1.html")
# print(html.read())
BS4O=BeautifulSoup(html_1, 'html')
# bs4Object.find_all('a')

# startsiden_html=urlopen("https://www.startsiden.no")
# startsiden=BeautifulSoup(startsiden_html, "html")

def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj=BeautifulSoup(html_1, "html")
        title=bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title=getTitle("http://wwww.pythonscraping.com/pages/page1.html")

# if title==None:
#     print("Title could not be found")
# else:
#     print(title)

      


# def gtitle(url):
#     bs4_object=BeautifulSoup(url, "html")
#     print(bs4_object.body)


html_2=urlopen("http://www.pythonscraping.com/pages/page3.html")
tn_gifts=BeautifulSoup(html_2,"html")

# for child in tn_gifts.find("table",{"id":"giftList"}).children:
#     print(child)


# for siblings in tn_gifts.find("table", {"id":"giftList"}).tr.next_siblings:
#     print(siblings)

# print(tn_gifts.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

images=tn_gifts.findAll("img",{"src":re.compile("\.\./img\/gifts/img.*.jpg")})
for image in images:
    print(image["src"])

# tn_gifts.findAll(lambda tag: len(tag.attrs)==2)
