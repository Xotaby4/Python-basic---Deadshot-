import asyncio
import csv
import requests
from random import choices
from time import time

from aiohttp import ClientSession
from bs4 import BeautifulSoup


def timer(func):
    """This function shows the execution time of
       the function object passed"""
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


@timer
async def aiohttp_get(url):
    """the function gets the page code asynchronously"""
    async with ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            return html


@timer
def get_film(html_film: BeautifulSoup) -> list:
    """Parse the title, year and link to the movie"""
    year = html_film.find('span').text[1:-1]
    name = html_film.find('a').string
    link = 'https://www.imdb.com' + html_film.find('a').get('href')
    return [year, name, link]


@timer
def get_description(page: str) -> str:
    """return film description"""
    soup = BeautifulSoup(page, 'html.parser')
    try:
        res = soup.find('span', class_='sc-16ede01-2').text
    except AttributeError:
        print(page)
        res = 'No find description'
    return res


@timer
def write_csv(list_films: list):
    with open('films.csv', 'w') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['Year', 'Name', 'Description'])
        for row in list_films:
            writer.writerow(row)


async def task(f_list: list):
    urls = [x[2] for x in f_list]
    tasks = [asyncio.create_task(aiohttp_get(x)) for x in urls]
    t = [await asyncio.wait(tasks)]
    for i, film in enumerate(f_list):
        film.pop()
        film.append(get_description(tasks[i].result()))
    print(f_list)
    write_csv(film_list)


if __name__ == '__main__':
    t1 = time()
    number_of_films = 10
    page = requests.get('https://www.imdb.com/chart/top/').text
    soup = BeautifulSoup(page, 'html.parser')
    ten_film_list = choices(soup.find_all('td', class_='titleColumn'), k=number_of_films)
    film_list = [get_film(ten_film_list.pop()) for i in range(number_of_films)]
    asyncio.run(task(film_list))
    t2 = time()
    print(f'Program executed in {(t2 - t1):.4f}s')
