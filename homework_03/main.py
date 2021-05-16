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
    create_tables,
    User,
    Post,
    add_row_in_table
)
import json
from jsonplaceholder_requests import (
    get_resource_body,
    USERS_DATA_URL,
    POSTS_DATA_URL
)

async def async_main():
    await create_tables()
    res = await asyncio.gather(
        get_resource_body(USERS_DATA_URL),
        get_resource_body(POSTS_DATA_URL),
        return_exceptions=True
    )
    j_users = json.loads(res[0])
    j_posts = json.loads(res[1])
    for t_user in j_users:
        user = User(id=t_user["id"],
                    name=t_user["name"],
                    username=t_user["username"],
                    email=t_user["email"])

        posts = list()
        for t_post in j_posts:
            post = Post(user_id = t_post["userId"],
                        title=t_post["title"],
                        body=t_post["body"])
            if t_post["userId"] == t_user["id"]:
                posts.append(post)
        user.posts = posts
        await add_row_in_table(user)

def main():
    asyncio.get_event_loop().run_until_complete(async_main())


if __name__ == "__main__":
    main()
