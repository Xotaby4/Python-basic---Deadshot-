from bs4 import BeautifulSoup
from random import randint
import requests, csv


def get_film(html_film: BeautifulSoup) -> list:
    year = html_film.find('span').text[1:-1]
    name = html_film.find('a').string
    link = 'https://www.imdb.com' + html_film.find('a').get('href')
    return [year, name, link]


def get_description(link: str) -> str:
    """return film description"""
    page = requests.get(link)
    #print(page.status_code)
    soup = BeautifulSoup(page.text, 'html.parser')
    try:
        res = soup.find('span', class_='sc-16ede01-2').text
    except AttributeError:
        print(link)
        res = 'No find description'
    return res

def write_csv(list_films):
    with open('films.csv', 'w') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['Year','Name','Description'])
        for row in list_films:
            writer.writerow(row)
if __name__ == '__main__':
    film_list = [0] * 10
    ten_random_number= set()
    while 10 > len(ten_random_number):
        ten_random_number.add(randint(0, 249))
    page = requests.get('https://www.imdb.com/chart/top/')
    print(page.status_code)
    soup = BeautifulSoup(page.text, 'html.parser')
    soup_film_list = soup.find_all('td', class_='titleColumn')
    for i in range(10):
        film_list[i] = (get_film(soup_film_list[ten_random_number.pop()]))
        film_list[i].append(get_description(film_list[i].pop()))
    write_csv(film_list)
