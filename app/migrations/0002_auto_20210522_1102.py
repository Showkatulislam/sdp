# Generated by Django 3.1.6 on 2021-05-22 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='area',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(upload_to='restaurent'),
        ),
    ]
