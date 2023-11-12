from bs4 import BeautifulSoup as BS
import requests
from base_parser import BaseParser

for page in range(1,10):
    url = ("https://vandrouki.by/page/"+str(page)+"/")
    data = requests.get(url).text
    soup = BS(data, features="html.parser")
    class Vandrouki(BaseParser):

        def abstr(url):
            print(False)

        def parser(self):

            article_names = soup.find_all('h2', class_= "entry-title")

            for name in article_names:
                info = (f"{name.a['title']}\n")
                with open(file = "article_names_from_vandrouki.txt", mode="a") as article_names:
                    article_names.write(info)

    Vandrouki.parser(data)

