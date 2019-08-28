from django.shortcuts import render
from phones.models import Phone, Samsung, Huawei, Apple


def add_phones(phone_list, context_data):
	

	for phone in phone_list:
		item = {}
		item["model"] = phone.phone_id.model
		item["price"] = phone.phone_id.price
		item["os"] = phone.phone_id.os
		item["cpu"] = phone.phone_id.cpu
		item["cores"] = phone.phone_id.cores
		item["ram"] = phone.phone_id.ram
		item["rom"] = phone.phone_id.rom
		item["camera"] = phone.phone_id.camera
		item["resolution"] = phone.phone_id.resolution
		item["battery"] = phone.phone_id.battery
		item["addons"] = []

		context_data[phone.phone_id.id] = item

	for phone in phone_list:

		context_data[phone.phone_id.id]["addons"].append(phone.addon)


def show_catalog(request):

    template = 'catalog.html'
    context = {}
    context["data"] = {}

    phone_fields = Phone._meta.fields
    huawei_all = Huawei.objects.all()
    samsung_all = Samsung.objects.all()
    apple_all = Apple.objects.all()

    add_phones(huawei_all, context["data"])
    add_phones(samsung_all, context["data"])
    add_phones(apple_all, context["data"])


    return render(
        request,
        template,
        context
    )
