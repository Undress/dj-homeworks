from django.contrib import admin
from phones.models import Phone, Samsung, Huawei, Apple


@admin.register(Phone, Samsung, Huawei, Apple)
class admin(admin.ModelAdmin):
	pass


# Register your models here.
