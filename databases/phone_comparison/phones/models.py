from django.db import models

# Create your models here.

class Phone(models.Model):

	model = models.CharField('Model', max_length=64)
	price = models.CharField('Price', max_length=64)
	os = models.CharField('OS', max_length=64)
	cpu = models.CharField('CPU', max_length=64)
	cores = models.IntegerField('Cores')
	ram = models.IntegerField('RAM')
	rom = models.IntegerField('Memory')
	camera = models.CharField('Camera', max_length=64)
	resolution = models.CharField('Resolution', max_length=64)
	battery = models.CharField('battery', max_length=64)


	def __str__(self):
		return self.model


class Samsung(models.Model):
	phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE)
	addon = models.CharField('Addon', max_length=64)
	



class Huawei(models.Model):
	phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE)
	addon = models.CharField('Addon', max_length=64)



class Apple(models.Model):
	phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE)
	addon = models.CharField('Addon', max_length=64)





