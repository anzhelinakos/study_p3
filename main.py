
class BaseParser():
    def get_data(url):
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
        raise ValueError(f"Error: {res.status_code}")
    @abstractmethod
    def abstr(self):



if __name__ == '__main__':
    data = _get_data(url)
    soup = BS(data,features="html.parser")
    pars = parser()


