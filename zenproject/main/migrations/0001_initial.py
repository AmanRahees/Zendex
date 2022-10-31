# Generated by Django 4.1.1 on 2022-10-13 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=250)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('Created_At', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
