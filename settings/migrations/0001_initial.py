# Generated by Django 4.2.7 on 2023-11-01 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Описание о нас')),
                ('descriptions', models.TextField(verbose_name='Описание о нас')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Фото о нас')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Названия курса')),
                ('descriptions', models.TextField(verbose_name='Описание курса')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Фото курса')),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок сайта')),
                ('descriptions', models.TextField(verbose_name='Описание сайта')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Фотография сайта')),
                ('logo', models.ImageField(upload_to='image/', verbose_name='Лого сайта')),
            ],
            options={
                'verbose_name': 'Настройка сайта',
                'verbose_name_plural': 'Настройки сайта',
            },
        ),
    ]
