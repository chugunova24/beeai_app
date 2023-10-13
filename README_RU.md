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
git clone МОЙ_РЕПОЗИТОРИЙ
```
2. Зайдите в папку проекта beeai_app
```
cd ПАПКА_ПРОЕКТА
```
3. Выполните следующую команду для сборки всех сервисов:

```
sudo docker-compose build --no-cache django && docker-compose up -d 
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

![Image alt](https://github.com/chugunova24/{repository}/raw/{branch}/{path}/image.png)[//]: # (![Иллюстрация к проекту]&#40;https://github.com/jon/coolproject/raw/master/image/image.png![img.png]&#40;img.png&#41;&#41;)

2. Попробуйте отправить еще один POST запрос с такими же свойствами. Тереперь
сервер вернет последний (от предыдущего запроса) вопрос из БД:

![Image alt](https://github.com/chugunova24/{repository}/raw/{branch}/{path}/image.png)[//]: # (![Иллюстрация к проекту]&#40;https://github.com/jon/coolproject/raw/master/image/image.png![img.png]&#40;img.png&#41;&#41;)

# Дополнительно: графический интерфейс PgAdmin4 <a name="Addition-PgAdmin"></a>


# Спасибо за внимание! <a name="Thanks"></a>
(что-то)