import asyncio
import json
from aiohttp_get import aiohttp_get_json


async def get_posts():
    print("Get posts started!")
    response = await aiohttp_get_json('http://jsonplaceholder.typicode.com/posts')
    file = open('posts.json', 'w')
    file.write(json.dumps(response))
    file.close()
    print("Get posts ended!")


async def get_comments():
    print("Get comments started!")
    response = await aiohttp_get_json('http://jsonplaceholder.typicode.com/comments')
    file = open('comments.json', 'w')
    file.write(json.dumps(response))
    file.close()
    print("Get comments ended!")



async def main():
    tasks = [get_posts(), get_comments()]
    await asyncio.gather(*tasks)


asyncio.run(main())