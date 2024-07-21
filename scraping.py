import urllib.request as url
import bs4
path="https://www.snapdeal.com/search?keyword=shoes&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail="

#print(url.urlopen(path))
#Make the HTTP request to the URL from where you want to scrap the data.
response=url.urlopen(path)
#pass your response inside bs4.BeautifulSoup
page=bs4.BeautifulSoup(response,features="html.parser")
#in return we get complete HTML of the requested webpage
#print(page)

#fetch one item
'''title=page.find('p',{'class' : 'product-title'})
print("Title: ",title.text)
price=page.find('span',{'class' : 'lfloat product-price'})
print("Price : ",price.text)'''


titleList=page.find_all('p',{'class' : 'product-title'})
priceList=page.find_all('span',{'class' : 'lfloat product-price'})

for i in range(len(titleList)):
    print("\nTitle : ",titleList[i].text)
    print("Price : ",priceList[i].text)
    print("\n==============================")