import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging

flipcart_url = "https://www.flipkart.com/search?q=" + "iphone12pro"
print(flipcart_url)

urlClient=urlopen(flipcart_url)

flipcart_page=urlClient.read()

flipcart_html=bs(flipcart_page,'html.parser')

bigbox=flipcart_html.findAll("div",{"class": "_1AtVbE col-12-12"})
print(len(bigbox))

del bigbox[0:2]
del bigbox[-3:]


for i in range(len(bigbox)):
    print("https://www.flipkart.com"+bigbox[i].div.div.div.a['href'])
    print('\n')

print(len(bigbox))  



