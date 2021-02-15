# Generated by Django 3.1.6 on 2021-02-15 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('key', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('key', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('publisher', models.TextField()),
                ('publish_date', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('cover', models.CharField(max_length=7)),
                ('isbn_10', models.CharField(max_length=10)),
                ('isbn_13', models.CharField(max_length=13)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('authors', models.ManyToManyField(to='store.Author')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
