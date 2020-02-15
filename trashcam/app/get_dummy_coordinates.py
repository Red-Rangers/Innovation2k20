import requests
from bs4 import BeautifulSoup as bs

def get_points():
    dummy_coord = []
    for x in range(1,9):
        url = f'https://www.latlong.net/category/cities-102-15-{x}.html'
        res = requests.get(url)
        soup = bs(res.text,'html.parser')
        row = soup.find_all('tr')
        for x in row:
            td = x.find_all('td')
            coord = [y.text for y in td[1:]]
            dummy_coord.append(coord)
    dict_coord = [{"loc":x[0],"lat":x[1],"long":x[2]} for x in dummy_coord if len(x) > 0]
    return dict_coord

if __name__ == '__main__':
    print(get_points())
