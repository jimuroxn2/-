import requests
from bs4 import BeautifulSoup
import urllib

#Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content,"html.parser")

#すべてのimgタグを検索し、リンクを取得する
for element in soup.find_all("img"):        #すべてのimgタグを検索
    src = element.get("src")                #src属性を取得

    #絶対URLと、ファイルを表示する
    image_url = urllib.parse.urljoin(load_url,src)
    filename = image_url.split("/")[-1]
    print(image_url,">>",filename)
