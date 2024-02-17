import requests
from bs4 import BeautifulSoup

#webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test1.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content,"html.parser")

#title,h2,liタグを検索して、その文字列を表示する
print(soup.find("title").text)
print(soup.find("h2").text)
print(soup.find("li").text)
