# Generated by Django 2.1.1 on 2019-08-12 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addon', models.CharField(max_length=64, verbose_name='Addon')),
            ],
        ),
        migrations.CreateModel(
            name='Huawei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addon', models.CharField(max_length=64, verbose_name='Addon')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=64, verbose_name='Model')),
                ('price', models.CharField(max_length=64, verbose_name='Price')),
                ('os', models.CharField(max_length=64, verbose_name='OS')),
                ('cpu', models.CharField(max_length=64, verbose_name='CPU')),
                ('cores', models.IntegerField(verbose_name='Cores')),
                ('ram', models.IntegerField(verbose_name='RAM')),
                ('rom', models.IntegerField(verbose_name='Memory')),
                ('camera', models.CharField(max_length=64, verbose_name='Camera')),
                ('resolution', models.CharField(max_length=64, verbose_name='Resolution')),
                ('battery', models.CharField(max_length=64, verbose_name='battery')),
            ],
        ),
        migrations.CreateModel(
            name='Samsung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addon', models.CharField(max_length=64, verbose_name='Addon')),
                ('phone_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone')),
            ],
        ),
        migrations.AddField(
            model_name='huawei',
            name='phone_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone'),
        ),
        migrations.AddField(
            model_name='apple',
            name='phone_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone'),
        ),
    ]
