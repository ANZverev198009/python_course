#todo:

#  Установить FLASK, установить SQLAlchemy
#  Настроить ORM на базу PostgresSQL
#  Для модели  БД "Система проверки задач" создать ORM модель. Сгенерировать ее в БД.
#  Переписать запросы с SQL на ORM


# https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application
# https://stackabuse.com/using-sqlalchemy-with-flask-and-postgresql/
# https://habr.com/ru/companies/yandex/articles/511892/

# Создать интерфейсы ввода GUI согласно бизнес логики.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import POSTGRES_URL

app= Flask(__name__)

print(POSTGRES_URL)
app.config['SQLALCHEMY_DATABASE_URI'] = str(POSTGRES_URL)

db = SQLAlchemy(app)
