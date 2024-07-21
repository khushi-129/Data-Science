
import urllib.request as url
import json

API_KEY='19d3f471046a4450b0eac081e26a2e38'
path=f"https://newsapi.org/v2/everything?q=tesla&from=2024-03-11&sortBy=publishedAt&apiKey={API_KEY}"

response=url.urlopen(path)
data=json.load(response)

#print(data)
articles=data['articles']

for i in range(len(articles)):
    print(articles[i]['title'])
    print(articles[i]['publishedAt'])
    print("==============================")