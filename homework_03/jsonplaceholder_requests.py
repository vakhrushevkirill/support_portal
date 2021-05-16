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
            return await response.json()
