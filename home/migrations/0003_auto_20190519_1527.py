# Generated by Django 2.2.1 on 2019-05-19 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_reises'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Reises',
        ),
    ]
