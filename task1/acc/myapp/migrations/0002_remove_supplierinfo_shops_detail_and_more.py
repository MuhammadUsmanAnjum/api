# Generated by Django 4.1.3 on 2022-12-13 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplierinfo',
            name='shops_detail',
        ),
        migrations.AddField(
            model_name='supplierinfo',
            name='shops_detail',
            field=models.ManyToManyField(to='myapp.shopdetail'),
        ),
    ]
