# Generated by Django 3.2.5 on 2021-07-07 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='meter',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('time_from', models.DateField(unique=True)),
                ('consumption', models.DecimalField(decimal_places=3, max_digits=7)),
                ('value', models.DecimalField(decimal_places=4, max_digits=7)),
            ],
        ),
    ]