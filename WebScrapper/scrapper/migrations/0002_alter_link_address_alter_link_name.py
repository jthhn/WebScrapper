# Generated by Django 5.1.5 on 2025-04-05 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='address',
            field=models.CharField(default='no_link', max_length=1000),
        ),
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(default='no_name', max_length=1000),
        ),
    ]
