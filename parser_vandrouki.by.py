from bs4 import BeautifulSoup as BS
import requests

for page in range(1,20):
    url = ("https://vandrouki.by/page/"+str(page)+"/")

    def get_data(url):
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
        raise ValueError(f"Error: {res.status_code}")

    def parser():
        data = get_data(url)
        soup = BS(data,features="html.parser")
        article_names = soup.find_all('h2', class_= "entry-title")

        for name in article_names:
            info = (f"{name.a['title']}\n")
            with open(file = "article_names.txt", mode="a") as article_names:
                article_names.write(info)

    parser()