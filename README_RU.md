Тестовое задание для комании Bewise.ai
==============
***Содержание:***
- [Введение](#Introduction)
- [Стек технологий](#Technology-stack)
- [Запуск контейнеров](#Run-container)
- [Тестирование API (пример с Postman)](#Testing-Api)
- [Дополнительно: графический интерфейс PgAdmin4](#Addition-PgAdmin)
- [Спасибо за внимание!](#Thanks)


# Введение <a name="Introduction"></a>
django_beeai - это мини-сервис, который принимает на вход число (количество уникальных вопросов с внешнего API сервиса, 
которые необходимо сохранить в базу данных) и возвращает
пользователю последний (от предыдущего запроса) вопрос из БД.

# Стек технологий <a name="Technology-stack"></a>

- Веб-фреймворк - [Django](https://www.djangoproject.com/)
- REST framework - [Django Rest Framework](https://www.django-rest-framework.org/)
- Инструмент управления для зависимости в Python - [Poetry](https://python-poetry.org/)
- Объектно-реляционная СУБД - [PostreSQL](https://www.postgresql.org/)
- Графический интерфейс к PostgreSQL - [Pgadmin4](https://www.pgadmin.org/download/)

# Запуск контейнеров <a name="Run-container"></a>
Предполагается, что у Вас уже установлен Docker, docker-compose.

1. Склонируйте репозиторий на свой компьютер с помощью команды:
```
git clone https://github.com/chugunova24/beeai_app
```
2. Зайдите в папку проекта:
```
cd beeai_app
```
3. Выполните одну из следующих команд для сборки всех сервисов в зависимости от версии Docker:

```
docker-compose up -d 
```
или:
```
docker compose up -d
```
Есть еще один вариант для запуска image без кеша: 
```
docker-compose build --no-cache django && docker-compose up -d
```
4. После завершения установки Вы сможете пройти по следующим адресам:
   * django_beeai:
        1)  http://0.0.0.0:7000/
        2)  http://0.0.0.0:7000/api/random/
   * pgadmin - http://0.0.0.0:5050/


# Тестирование API (пример с Postman) <a name="Testing-Api"></a>

Предполагается, что у Вас уже установлена программа Postman.

1. Создайте новый POST запрос по URL: http://0.0.0.0:7000/api/random/. 
Во вкладке "Body" введите ключ:пару "count":5, затем нажмите на кнопку
"Send". Самый первый запрос к серверу вернет пустой объект, так как 
таблица базы данных будет пуста:



<img src="https://github.com/chugunova24/beeai_app/blob/master/img_readme/postman_null.png" />

2. Попробуйте отправить еще один POST запрос с такими же свойствами. Тереперь
сервер вернет последний (от предыдущего запроса) вопрос из БД:

![Image alt](https://github.com/chugunova24/beeai_app/blob/master/img_readme/postman_result.png)

# Дополнительно: графический интерфейс PgAdmin4 <a name="Addition-PgAdmin"></a>

1. Перейдите по ссылке http://0.0.0.0:5050/ в браузере. Авторизуйтесь под логином <b>t.chugunova24@gmail.com</b> и паролем <b>123456</b>:

2. Создайте новый сервер, назовите его <b>beeai_server</b> например:

<img src="https://github.com/chugunova24/beeai_app/blob/master/img_readme/create_server.png" style="width:70%;height:70%"/>

3. Создайте новое подключение к нашей базе данных Postgres. В поле hostname введите <b>postgres_beeai</b>,
в username введите <b>postgres</b>, в поле password <b>123456</b>:


<img src="https://github.com/chugunova24/beeai_app/blob/master/img_readme/connect_db.png" style="width:70%;height:70%"/>

4. Результат:

<img src="https://github.com/chugunova24/beeai_app/blob/master/img_readme/pg_result.png" style="width:70%;height:70%"/>


# Спасибо за внимание! <a name="Thanks"></a>

<img src="https://github.com/chugunova24/beeai_app/blob/master/img_readme/MkK1g1ban9d1A9N04A.gif" style="width:70%;height:70%"/>

