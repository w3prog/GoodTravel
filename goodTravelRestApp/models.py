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
    region = models.CharField(max_length=200, verbose_name="Регион", null=True)
    locality = models.CharField(max_length=200, verbose_name="Населенный пункт")
    address = models.CharField(max_length=300, verbose_name="Адрес в населенном пункте")
    coordinates = models.TextField(verbose_name="Координаты")


class Plan(models.Model):
    CATEGORIES = (
        (1, 'Экономный'),
        (2, 'Средний'),
        (3, 'Люкс'),
    )
    name = models.CharField(max_length=200, verbose_name="Название")
    creator = models.ForeignKey(User1)
    budget = models.CharField(choices=CATEGORIES, verbose_name="Бюджет", max_length=500, )
    city = models.CharField(max_length=200, verbose_name="Город")


class Feature(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    plan = models.ForeignKey(Plan)


class Place(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Название")
    type = models.CharField(max_length=200, verbose_name="Тип объекта")
    description = models.TextField(verbose_name="Описание")
    address = models.OneToOneField(Address)
    image = models.CharField(max_length=500, verbose_name="Основное изображение", null=True)


class Service(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Название")
    price = models.CharField(max_length=200, verbose_name="Цена")
    start_time = models.TimeField(verbose_name="Время начала", null=True)
    end_time = models.TimeField(verbose_name="Время конца", null=True)
    image = models.CharField(max_length=500, verbose_name="Ссылка на изображение", null=True)
    place = models.ForeignKey(Place)


class PlanPlace(models.Model):
    date = models.DateField(verbose_name="Дата")
    start_time = models.TimeField(verbose_name="Время начала")
    plan = models.ForeignKey(Plan)
    service = models.ForeignKey(Service)
