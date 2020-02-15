import requests
from bs4 import BeautifulSoup as bs

def get_points():
    dummy_coord = []
    url = 'https://www.latlong.net/category/cities-102-15-1.html'
    res = requests.get(url)
    soup = bs(res.text,'html.parser')
    row = soup.find_all('tr')
    for x in row:
        td = x.find_all('td')
        coord = [y.text for y in td[1:]]
        dummy_coord.append(coord)
    dict_coord = [{"lat":x[0],"long":x[1]} for x in dummy_coord if len(x) > 0]
    return dict_coord

if __name__ == '__main__':
    print(get_points())
