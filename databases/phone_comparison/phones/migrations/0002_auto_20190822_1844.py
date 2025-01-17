# Generated by Django 2.1.1 on 2019-08-22 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apple',
            name='addon',
        ),
        migrations.RemoveField(
            model_name='huawei',
            name='addon',
        ),
        migrations.RemoveField(
            model_name='samsung',
            name='addon',
        ),
        migrations.AddField(
            model_name='apple',
            name='face_id',
            field=models.CharField(default='no', max_length=64, verbose_name='FaceId'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apple',
            name='smart_touch',
            field=models.CharField(default='no', max_length=64, verbose_name='3dTouch'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='huawei',
            name='flashlight',
            field=models.CharField(default='no', max_length=64, verbose_name='flashlight'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='huawei',
            name='lense',
            field=models.CharField(default='no', max_length=64, verbose_name='Lense'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='samsung',
            name='bluetooth',
            field=models.CharField(default='no', max_length=64, verbose_name='Bluetooth'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='samsung',
            name='touch_id',
            field=models.CharField(default='no', max_length=64, verbose_name='WiFi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='samsung',
            name='wifi',
            field=models.CharField(default='no', max_length=64, verbose_name='WiFi'),
            preserve_default=False,
        ),
    ]
