from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.AutoField(primary_key=True)
    name = models.CharField('name', max_length=64)
    price = models.CharField('price', max_length=64)
    image = models.CharField('image', max_length=128)
    release_date = models.DateField('release_date')
    lte_exists = models.BooleanField('lte_exists')
    slug = models.CharField('slug', max_length=64)
 
