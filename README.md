# api_final
## Гений написавыший этот проект : Лесков Максим
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram_backend.git
```

```
cd 
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Описание проекта, основные функции:

Проект написан на основе фреймворка Django и Django Rest Framework, проект сделан как некая платформа для общения, в основных функциях есть:

Написание постов и комментариев к ним от других пользователей, так же присвоение поста к группе связанных одной идеей или темой. Есть реализованная модель подписок.

Доступ к созданию имеют только аутентифицированные пользователи, доступ к изменинению, частичному изменинию или удалению  имеют только авторы постов или комментариев.


## Plugins

```
Django==3.2.16
pytest==6.2.4
pytest-pythonpath==0.7.3
pytest-django==4.4.0
djangorestframework==3.12.4
djangorestframework-simplejwt==4.7.2
django-filter==23.5
djoser==2.1.0
Pillow==9.3.0
PyJWT==2.1.0
requests==2.26.0
```

## Примеры запросов и ответов
Post
```
http://.../api/v1/posts/
GET

{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
{}
]
}
```

```
http://.../api/v1/posts/
POST
{
"text": "string",
"image": "string",
"group": 0
}
```

```
http://.../api/v1/posts/{id}/
GET
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```
```
http://.../api/v1/posts/{id}/
PUT
{
"text": "string",
"image": "string",
"group": 0
}
```
```
http://.../api/v1/posts/{id}/
PATCH
{
"text": "string",
"image": "string",
"group": 0
}
```
```
http://.../api/v1/posts/{id}/
DELETE

HTTP response 201
```

```
http://.../api/v1/posts/{post_id}/comments/
GET
[
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
]
```
```
http://.../api/v1/posts/{post_id}/comments/
POST
{
"text": "string"
}
```
```
http://.../api/v1/posts/{post_id}/comments/{id}/
GET
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
```
```
http://.../api/v1/posts/{post_id}/comments/{id}/
PUT
{
"text": "string"
}
```
```
http://.../api/v1/posts/{post_id}/comments/{id}/
PATCH
{
"text": "string"
}
```
```
http://.../api/v1/posts/{post_id}/comments/{id}/
PUT
DELETE

HTTP response 201
```
```
http://.../api/v1/groups/
GET
[
{
"id": 0,
"title": "string",
"slug": "string",
"description": "string"
}
]
```
```
http://.../api/v1/groups/{id}/
GET
[
{
"id": 0,
"title": "string",
"slug": "string",
"description": "string"
}
]
```
```
http://127.0.0.1:8000/api/v1/follow/
GET
[
{
"user": "string",
"following": "string"
}
]
```
```
http://127.0.0.1:8000/api/v1/follow/
POST
{
"following": "string"
}
```
```
http://.../api/v1/jwt/create/
POST
{
"username": "string",
"password": "string"
}
```
```
http://.../api/v1/jwt/refresh/
POST
{
"refresh": "string"
}
```
```
http://.../api/v1/jwt/ferify/
POST
{
"token": "string"
}
```

