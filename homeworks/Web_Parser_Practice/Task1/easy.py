import aiohttp, asyncio
from time import time

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

async def aiohttp_get(url):
    """Nothing to see here, carry on ..."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            return html


@timer
async def task_creator(urls: list):
    tasks = [asyncio.create_task(aiohttp_get(x)) for x in urls]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    url_list = [
        'https://www.imdb.com/title/tt0111161/',
        'https://www.imdb.com/title/tt0050083/',
        'https://www.imdb.com/title/tt0468569/'
    ]
    asyncio.run(task_creator(url_list))
    pass
