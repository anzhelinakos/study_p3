from bs4 import BeautifulSoup as BS
import requests
from base_parser import BaseParser

url = ("https://www.redeyerecords.co.uk/funk-hip-hop-soul/new-releases")

class Redeyerecords(BaseParser):

    def abstr(url):
        print(False)
    def parser(self):
        vinil_info = soup.find_all(attrs = {"class":{"artist", "tracks", "label", "price"}})
        artist_vinil_info = soup.find_all(attrs={"class": {"artist"}})
        track_vinil_info = soup.find_all( attrs={"class": {"tracks"}})
        label_vilil_info = soup.find_all(attrs={"class": {"label"}})
        price_vinil_info = soup.find_all(attrs={"class": {"price"}})
        v_info = []
        for a in range (len(artist_vinil_info)):
            v_info = ({
                "artist": artist_vinil_info[a].text,
                "track": track_vinil_info[a].text,
                "label": label_vilil_info[a].text,
                "price": price_vinil_info[a].text
            })
            print(v_info)



if __name__ == '__main__':
    data = requests.get(url).text
    soup = BS(data,features="html.parser")
    Redeyerecords.parser(data)
    Redeyerecords.abstr(url)


