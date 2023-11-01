from bs4 import BeautifulSoup as BS
import requests
from base_parser import BaseParser
url = ("https://meteo.by/minsk/")

class Meteo(BaseParser):
    def abstr(self, url):
        print(url+url)


def parser():

    days = ['day0', 'day1', 'day2','day3', 'day4', 'day5', 'day6', 'day7', 'day8', 'day9']
    weather_date = soup.find_all('p', class_= "date")
    weather_date_info = dict(zip(days,[w.text for w in weather_date]))
    weather = soup.find_all('td', class_="temp")
    weather_info = [w.text for w in weather]
    def changeinfowiew(weather_info):
        listtodelate = [" ","\n","\r"]
        for i in range (len(listtodelate)):
            for j in range (len(weather_info)):
                weather_info[j] = weather_info[j].replace(listtodelate[i],"")
        return weather_info

    changeinfowiew(weather_info)
    weather_info = dict(zip(days,[weather_info[0]+" "+weather_info[1]+" "+weather_info[2]+" "+weather_info[3],
                    weather_info[4]+" "+weather_info[5]+" "+weather_info[6]+" "+weather_info[7],
                    weather_info[8]+" "+weather_info[9]+" "+weather_info[10]+" "+weather_info[11],
                    weather_info[12]+" "+weather_info[13]+" "+weather_info[14]+" "+weather_info[15],
                    weather_info[16]+" "+weather_info[17]+" "+weather_info[18]+" "+weather_info[19],
                    weather_info[20]+" "+weather_info[21]+" "+weather_info[22]+" "+weather_info[23],
                    weather_info[24]+" "+weather_info[25]+" "+weather_info[26]+" "+weather_info[27],
                    weather_info[28]+" "+weather_info[29]+" "+weather_info[30]+" "+weather_info[31],
                    weather_info[32]+" "+weather_info[33]+" "+weather_info[34]+" "+weather_info[35],
                    weather_info[36]+" "+weather_info[37]+" "+weather_info[38]+" "+weather_info[39]]))

    for day in days:
        infostring = f"Прогноз погоды на {weather_date_info[day]}  -  {weather_info[day]}"
        print(infostring)


if __name__ == '__main__':
    Meteo()
    data = requests.get(url).text
    soup = BS(data,features="html.parser")
    parser()