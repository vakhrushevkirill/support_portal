"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp
import asyncio

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_resource_body(url_resource):
    html = None
    async with aiohttp.ClientSession() as session:
        async with session.get(url_resource) as response:
            html = await response.text()
    return html


async def get_users_and_posts():
    res = await asyncio.gather(
        get_resource_body(USERS_DATA_URL),
        get_resource_body(POSTS_DATA_URL)
    )

def get_resource(url_resource):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(get_resource_body(url_resource))



#data = get_resource(USERS_DATA_URL)
#print(data)

#asyncio.run((get_users_and_posts()))