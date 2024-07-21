import urllib.request as url
import json

print(''' 
    1. Top Headlines
    2. Business
    3. Entertainment
    4. Health
    5. Sports
    6. Science
    7. Technology

''')

choice=input("Enter your Choice : ")
if choice=='1':
    path="https://newsapi.org/v2/top-headlines?country=in&apiKey=19d3f471046a4450b0eac081e26a2e38"
else:
    categories={"2": "business", "3": "entertainment","4": "health","5": "sports","6": "science","7":"technology"}
    category=categories[choice]

    path=f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey=19d3f471046a4450b0eac081e26a2e38"

response=url.urlopen(path)
data=json.load(response)

articles=data['articles']

for i in range(len(articles)):
    print(articles[i]['title'])
    print(articles[i]['publishedAt'])
    print("==============================")