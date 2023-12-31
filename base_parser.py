from abc import ABC, abstractmethod
import requests


class BaseParser(ABC):

    def __init__(self):
        pass

    def get_data(url):
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
        raise ValueError(f"Error: {res.status_code}")

    @abstractmethod
    def abstr(url):
        print(True)

