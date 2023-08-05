import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging
pname=input(str("Enter Product Name:"))
flipcart_url = f"https://www.flipkart.com/search?q={pname}" 
print(flipcart_url)

urlClient=urlopen(flipcart_url)

flipcart_page=urlClient.read()

flipcart_html=bs(flipcart_page,'html.parser')

bigbox=flipcart_html.findAll("div",{"class": "_1AtVbE col-12-12"})
#print(len(bigbox))

del bigbox[0:2]
del bigbox[-3:]


#for i in range(len(bigbox)):
productlink="https://www.flipkart.com"+bigbox[3].div.div.div.a['href']
print(productlink)

product_req=requests.get(productlink)

product_html=bs(product_req.text,'html.parser')
#print(product_req.text+"\n")

product_box=product_html.findAll('div',{'class':'_16PBlm'})
#print((product_box))
del product_box[-1:]
allreviewes=[]
for i in product_box:
    # print("Reviewer Name:"+i.div.find('p',{'class':'_2sc7ZR _2V5EHH'}).text)
    # print("Rating:"+i.div.div.div.div.text)
    # print("Comment:"+i.div.div.div.p.text)
    # print("Discription:"+i.div.div.find_all('div',{"class":""}))
    # print("=================================")
    reviews={
        "Reviewer Name": i.div.find('p',{'class':'_2sc7ZR _2V5EHH'}).text,
        "Rating":i.div.div.div.div.text,
        "Comment":i.div.div.div.p.text,
        "Discription":i.div.div.find('div',{"class":""}).text
    }
    allreviewes.append(reviews)
    

print(allreviewes)