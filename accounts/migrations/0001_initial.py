# Generated by Django 2.2.1 on 2019-05-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
    ]
