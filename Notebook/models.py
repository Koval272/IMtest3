from django.db import models


class Notebook(models.Model):
    audience = models.IntegerField('Номер аудитории', default = 0)
    brand = models.CharField('Бренд', max_length=50)
    model = models.CharField('Модель', max_length=50)
    tp = models.CharField('Тип', max_length=50)
    cpu = models.CharField('Процессор', max_length=50)
    gpu = models.CharField('Тип видеокарты', max_length=50)
    ram = models.IntegerField('Объем оперативной памяти, ГБ')
    state = models.CharField('Состояние', max_length=50)
    date = models.DateField('Приобретен')
    use = models.DateField('Введен в эксплуатацию')
    person = models.CharField('Ответветственное лицо', max_length=50)
    term = models.CharField('Срок амортизации', max_length=50)

class Repairs(models.Model):
    _brand = models.CharField('Бренд', max_length=50)
    _model = models.CharField('Модель', max_length=50)
    cause = models.CharField('Причина', max_length=50)
    _date = models.DateField('Дата поступления')