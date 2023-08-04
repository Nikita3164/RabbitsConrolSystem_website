from django.apps import AppConfig
from django.db import connections


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'


def get_rabbits():
    rbt_connection = connections['rabbits']
    with rbt_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM rabbits_group_1")
            row = cursor.fetchall()     # получаем одну строку
            return row