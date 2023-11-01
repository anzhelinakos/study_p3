from abc import ABC, abstractmethod

class BaseParser(ABC):
    def get_data(url):
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
        raise ValueError(f"Error: {res.status_code}")

    @abstractmethod
    def abstr(self, url):
        print(True)
