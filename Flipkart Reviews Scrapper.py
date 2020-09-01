import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
print("Please Enter Query" , '\n',"(Ex: motorola, iphone, furniture.(No Space allowed b/w Characters))")
search = input()
print("Enter Maxmium Page Numbers to Search",'\n'"(Ex: 10 , 20 , 30 , 50.)")
maxpage = int(input())
productLink = []
for j in range(0,maxpage):
   j = str(j)
   pages = 'https://www.flipkart.com/search?q=+++'+search+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page='+j
   uClient = uReq(pages)
   flipkartPage = uClient.read()
   uClient.close()
   flipkart_html = bs(flipkartPage, "html.parser")
   bigboxes = flipkart_html.findAll("div", {"class": "bhgxx2 col-12-12"})
   del bigboxes[0:2]  # remove useless boxes
   try:
    for i in range(0,23):
        link = bigboxes[i]
        productLink.append("https://www.flipkart.com" + link.div.div.div.a['href'])
   except :
        print("Maximum Available Pages =" , int(j)+1 )
        break
print("Total Scrapped Pages =" , int(j)+1 )
print('Total' ,search ,'items collected =',len(productLink))

total_comments = []
print("Scrapping Review = ",len(productLink)*10)
for i in range(0,len(productLink)):
  productLink[0]
  prodRes = requests.get(productLink[0])
  prodRes.encoding='utf-8'
  prod_html = bs(prodRes.text, "html.parser")
  commentboxes = prod_html.find_all('div', {'class': "_3nrCtb"})
  for i in range(0,10):
    commentbox=commentboxes[i]
    comtag = commentbox.div.div.find_all('div', {'class': ''})
                        #custComment.encode(encoding='utf-8')
    total_comments.append(comtag[0].div.text)
  print('Reviews Collected =',len(total_comments),'/',len(productLink)*10)
x = pd.DataFrame(data = total_comments)
x.to_csv(search +'_reviews'+'.csv')
print('File Saved')