# Generated by Django 3.2.5 on 2021-07-12 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('username', models.CharField(blank=True, default='', max_length=100)),
                ('email', models.CharField(blank=True, default='', max_length=100)),
                ('address_street', models.CharField(blank=True, default='', max_length=100)),
                ('address_suite', models.CharField(blank=True, default='', max_length=100)),
                ('address_city', models.CharField(blank=True, default='', max_length=100)),
                ('address_zipcode', models.CharField(blank=True, default='', max_length=100)),
                ('address_geo_lat', models.DecimalField(decimal_places=2, max_digits=9)),
                ('address_geo_lng', models.DecimalField(decimal_places=2, max_digits=9)),
                ('phone', models.CharField(blank=True, default='', max_length=100)),
                ('website', models.CharField(blank=True, default='', max_length=100)),
                ('company_name', models.CharField(blank=True, default='', max_length=100)),
                ('company_catchPhrase', models.CharField(blank=True, default='', max_length=100)),
                ('company_bs', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
