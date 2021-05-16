"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from models import (
    Session,
    User,
    Post,
    Base,
    engine
)
from jsonplaceholder_requests import (
    get_resource_body,
    USERS_DATA_URL,
    POSTS_DATA_URL
)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def add_row_in_table(value):
    async with Session() as session:
        async with session.begin():
            session.add(value)
        await session.commit()


async def async_main():
    await create_tables()
    users_data, posts_data = await asyncio.gather(
        get_resource_body(USERS_DATA_URL),
        get_resource_body(POSTS_DATA_URL),
    )

    await add_users(users_data)
    await add_posts(posts_data)


async def add_users(users_data):
    for t_user in users_data:
        user = User(id=t_user["id"],
                    name=t_user["name"],
                    username=t_user["username"],
                    email=t_user["email"])
        await add_row_in_table(user)


async def add_posts(posts_data):
    for t_post in posts_data:
        post = Post(user_id = t_post["userId"],
                    title=t_post["title"],
                    body=t_post["body"])
        await add_row_in_table(post)


def main():
    asyncio.get_event_loop().run_until_complete(async_main())


if __name__ == "__main__":
    main()
