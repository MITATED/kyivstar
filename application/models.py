from django.db import models
from django.contrib.auth.models import User


class AppTypes(models.Model):
    types = models.CharField(max_length=64, verbose_name="Название типа")
    abbr = models.CharField(max_length=3, verbose_name="Абревиатура типа")

    def __str__(self):
        return self.types

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class AppStatus(models.Model):
    status = models.CharField(max_length=15, verbose_name="Статус")
    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class AppError(models.Model):
    error = models.CharField(max_length=15, verbose_name="Ошибка")
    def __str__(self):
        return self.error

    class Meta:
        verbose_name = 'Ошибка'
        verbose_name_plural = 'Ошибки'


class AppSuccess(models.Model):
    success = models.CharField(max_length=32, verbose_name="Тип работы")
    def __str__(self):
        return self.success

    class Meta:
        verbose_name = 'Тип работы'
        verbose_name_plural = 'Тип работ'


class Street(models.Model):
    # city = models.IntegerField(verbose_name="Улица")
    street = models.CharField(verbose_name="Улица", max_length=256)

    def __str__(self):
        return self.street

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'


class House(models.Model):
    street = models.ForeignKey(Street, on_delete='', verbose_name="Улица")
    house = models.CharField(verbose_name="Дом", max_length=5)

    def __str__(self):
        return "%s, д.%s" % (self.street, self.house)

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'


class Apartment(models.Model):
    house = models.ForeignKey(House, on_delete='', verbose_name="Дом")
    apartment = models.CharField(verbose_name="Квартира", max_length=15)

    def __str__(self):
        return "%s. кв.%s" % (self.house, self.apartment)

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'



class Application(models.Model):
    date = models.DateField(verbose_name="Дата")
    types = models.ForeignKey(AppTypes, on_delete='', verbose_name="Тип")
    time = models.TimeField(verbose_name="Время")
    order = models.IntegerField(verbose_name="Наряд")
    port = models.IntegerField(verbose_name="Порт", null=True, blank=True)
    problem = models.CharField(verbose_name="Проблема", max_length=2048, null=True, blank=True)
    personal_account = models.IntegerField(verbose_name="Личный счет")
    address = models.ForeignKey(Apartment, on_delete='', verbose_name="Адрес")
    telephone = models.CharField(verbose_name="Номер телефона", max_length=256)
    tariff = models.CharField(verbose_name="Тариф", max_length=256, null=True, blank=True)
    router = models.BooleanField(verbose_name="Роутер")
    router_pro = models.BooleanField(verbose_name="Роутер ПРО")
    tuner = models.BooleanField(verbose_name="Тюнер")
    activation = models.BooleanField(verbose_name="активация")
    master = models.ForeignKey(User, on_delete='', verbose_name="Мастер")
    status = models.ForeignKey(AppStatus, on_delete='', verbose_name="Статус")
    error = models.ForeignKey(AppError, on_delete='', verbose_name="Причины", null=True, blank=True)
    success = models.ForeignKey(AppSuccess, on_delete='', verbose_name="Тип работы", null=True, blank=True)
    comment = models.CharField(verbose_name="Комментарий отчета", max_length=2048, null=True, blank=True)
    connectors = models.IntegerField(verbose_name="Коннекторы", default=0)
    utp_internal = models.IntegerField(verbose_name="Внутренний кабель", default=0)
    utp_external = models.IntegerField(verbose_name="Внешний кабель", default=0)
    num_router = models.CharField(verbose_name="Серийник роутера", max_length=15, null=True, blank=True)
    num_tuner = models.CharField(verbose_name="MAC тюнера", max_length=50, null=True, blank=True)
    comments = models.CharField(verbose_name="Комментарий", max_length=2048, null=True, blank=True)

    def __str__(self):
        return self.address.__str__()

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
