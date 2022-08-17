import aiohttp
import asyncio
import csv
import requests
from random import choices
from time import time

from aiohttp import ClientResponse
from bs4 import BeautifulSoup


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
async def aiohttp_get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            return html


@timer
def get_film(html_film: BeautifulSoup) -> list:
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
        print("url")
        res = 'No find description'
    return res


@timer
def write_csv(list_films: list):
    with open('films.csv', 'w') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['Year', 'Name', 'Description'])
        for row in list_films:
            writer.writerow(row)


async def task_creator(urls: list):
    tasks = [asyncio.create_task(aiohttp_get(x)) for x in urls]
    t = [await asyncio.wait(tasks)]
    des_list =[get_description(t[0][0].pop().result()) for i in range(3)]
    return des_list


if __name__ == '__main__':
    t1 = time()
    film_list = [0] * 10
    page = requests.get('https://www.imdb.com/chart/top/').text
    soup = BeautifulSoup(page, 'html.parser')
    ten_film_list = choices(soup.find_all('td', class_='titleColumn'), k=10)
    url_list = [get_film(x)[2] for x in ten_film_list]
    asyncio.run(task_creator([url_list]))
    for i in range(len(ten_film_list)):
        film_list[i] = get_film(ten_film_list.pop())
        film_list.append(get_description(film_list.pop()))
    write_csv(film_list)
    t2 = time()
    print(f'Program executed in {(t2 - t1):.4f}s')
