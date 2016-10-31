from django.db import models


# Create your models here.
class User1(models.Model):
    login = models.CharField(max_length=200, unique=True, verbose_name="Логин")
    password = models.CharField(max_length=200, verbose_name="Пароль")
    list_devices = models.TextField(verbose_name="Список устройств")
    language = models.CharField(max_length=100, verbose_name="Язык")
    budget = models.CharField(max_length=100, verbose_name="Бюджет")
    first_installation = models.DateField(verbose_name="Дата установки")


class Address(models.Model):
    country = models.CharField(max_length=200, verbose_name="Страна")
    region = models.CharField(max_length=200, verbose_name="Регион")
    locality = models.CharField(max_length=200, verbose_name="Населенный пункт")
    address = models.CharField(max_length=300, verbose_name="Адрес в населнном пункте")
    coordinates = models.TextField(verbose_name="Координаты")


class Plan(models.Model):
    CATEGORIES = (
        (1, 'Экономный'),
        (2, 'Средний'),
        (3, 'Люкс'),
    )
    name = models.CharField(max_length=200, verbose_name="Название", unique=True)
    dates = models.CharField(max_length=200, verbose_name="Даты")
    creator = models.ForeignKey(User1)
    budget = models.CharField(choices=CATEGORIES, verbose_name="Бюджет", max_length=500, )
    city = models.CharField(max_length=200, verbose_name="Город")
    users = models.TextField(verbose_name="Пользователи в плане")
    features = models.TextField(verbose_name="Особенности")


class Date(models.Model):
    date = models.DateField(verbose_name="Дата")
    route = models.TextField(verbose_name="Маршрут")
    plan = models.ForeignKey(Plan)


class Place(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Название")
    type = models.CharField(max_length=200, verbose_name="Тип объекта")
    description = models.TextField(verbose_name="Описание")
    address = models.OneToOneField(Address)
    image = models.CharField(max_length=500, verbose_name="Основное изображение")
    day = models.ForeignKey(Date)






