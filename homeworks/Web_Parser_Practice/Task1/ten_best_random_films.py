from bs4 import BeautifulSoup
from random import randint
from time import time
import csv, asyncio, aiohttp


def timer(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func

@timer
async def get_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)
            return await response.text()

@timer
def get_film(html_film: BeautifulSoup) -> list:
    year = html_film.find('span').text[1:-1]
    name = html_film.find('a').string
    link = 'https://www.imdb.com' + html_film.find('a').get('href')
    return [year, name, link]


@timer
def get_description(url: str) -> str:
    """return film description"""
    page = asyncio.run(get_html(url))
    soup = BeautifulSoup(page, 'html.parser')
    try:
        res = soup.find('span', class_='sc-16ede01-2').text
    except AttributeError:
        print(url)
        res = 'No find description'
    return res


@timer
def write_csv(list_films):
    with open('films.csv', 'w') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['Year', 'Name', 'Description'])
        for row in list_films:
            writer.writerow(row)


if __name__ == '__main__':
    t1 = time()
    film_list = [0] * 10
    ten_random_number = set()
    while 10 > len(ten_random_number):
        ten_random_number.add(randint(0, 249))
    page = asyncio.run(get_html('https://www.imdb.com/chart/top/'))
    soup = BeautifulSoup(page, 'html.parser')
    soup_film_list = soup.find_all('td', class_='titleColumn')
    for i in range(10):
        film_list[i] = (get_film(soup_film_list[ten_random_number.pop()]))
        film_list[i].append(get_description(film_list[i].pop()))
    write_csv(film_list)
    t2 = time()
    print(f"time = {(t2-t1):4f}")