# Generated by Django 3.2.9 on 2021-11-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=30, unique=True)),
                ('country', models.CharField(max_length=30)),
                ('number_of_pages', models.IntegerField()),
                ('publisher', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('authors', models.ManyToManyField(to='api.Authors')),
            ],
        ),
    ]
