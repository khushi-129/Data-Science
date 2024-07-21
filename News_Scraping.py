#Scraping 
import urllib.request as url
import json

API_key="19d3f471046a4450b0eac081e26a2e38"

path=f"https://newsapi.org/v2/everything?q=apple&from=2024-03-09&to=2024-03-09&sortBy=popularity&apiKey={API_key}"

response=url.urlopen(path)
data=json.load(response)

articles=data['articles']

for i in range(len(articles)):
    print(articles[i]['titile'])
    print("==============================")