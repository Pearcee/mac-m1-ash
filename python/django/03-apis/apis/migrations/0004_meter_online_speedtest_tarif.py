# Generated by Django 3.2.4 on 2021-06-25 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_comment_geeksmodel_hero_post_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='meter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumption', models.DecimalField(decimal_places=3, max_digits=3)),
                ('Timestamp', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='online',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.DateTimeField(null=True)),
                ('ip', models.CharField(max_length=62)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='speedtest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServerID', models.IntegerField()),
                ('Timestamp', models.DateTimeField(null=True)),
                ('Distance', models.DecimalField(decimal_places=8, max_digits=12)),
                ('Ping', models.DecimalField(decimal_places=3, max_digits=3)),
                ('Download', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Upload', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ip', models.CharField(max_length=62)),
            ],
        ),
        migrations.CreateModel(
            name='tarif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=3, max_digits=3)),
                ('Timestamp', models.DateTimeField(null=True)),
            ],
        ),
    ]
