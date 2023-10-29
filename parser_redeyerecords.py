from bs4 import BeautifulSoup as BS
import requests

url = ("https://www.redeyerecords.co.uk/funk-hip-hop-soul/new-releases")

def _get_data(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.text
    raise ValueError(f"Error: {res.status_code}")

def parser():
    selector = "body"
    main_box = soup.find(selector)
    table = main_box.find("div", attrs={"class": "releaseGrid grid"})
    items = table.select("div>div")
    for item in items:
        info = {
            "artist": item.findAll("p",attrs={"class": "artist"}),
            "track": item.findAll("p", attrs={"class": "tracks"}),
            "label": item.findAll("p", attrs={"class": "label"}),
            "price": item.findAll("div", attrs={"class": "price"})
        }
        print(info)



if __name__ == '__main__':
    data = _get_data(url)
    soup = BS(data,features="html.parser")
    pars = parser()


