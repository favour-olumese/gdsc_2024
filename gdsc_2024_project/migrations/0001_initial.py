# Generated by Django 4.2.11 on 2024-04-08 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=150)),
                ('book_name', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=350)),
            ],
        ),
    ]
