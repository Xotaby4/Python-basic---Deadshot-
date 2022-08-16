from time import time

import aiohttp
import asyncio


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
    """Nothing to see here, carry on ..."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            print(url, response.status)
            return html


@timer
async def task_creator(urls: list):
    tasks = [asyncio.create_task(aiohttp_get(x)) for x in urls]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    t1 = time()
    url_list = [
        'https://www.imdb.com/title/tt0111161/',
        'https://www.imdb.com/title/tt0050083/',
        'https://www.imdb.com/title/tt0468569/'
    ]
    asyncio.run(task_creator(url_list))
    t2 = time()
    print(f'Program executed in {(t2 - t1):.4f}s')

# import asyncio
# import time
# from aiohttp import ClientSession
#
#
# async def get_weather(city):
#     async with ClientSession() as session:
#         url = f'http://api.openweathermap.org/data/2.5/weather'
#         params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}
#
#         async with session.get(url=url, params=params) as response:
#             weather_json = await response.json()
#             return f'{city}: {weather_json["weather"][0]["main"]}'
#
#
# async def main(cities_):
#     tasks = []
#     for city in cities_:
#         tasks.append(asyncio.create_task(get_weather(city)))
#
#     results = await asyncio.gather(*tasks)
#
#     for result in results:
#         print(result)
#
#
# cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
#           'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']
#
# print(time.strftime('%X'))
#
# asyncio.run(main(cities))
#
# print(time.strftime('%X'))
