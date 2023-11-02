from django.db import models

# Create your models here.

class Index(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок сайта'
    )
    descriptions = models.TextField(
        verbose_name='Описание сайта'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фотография сайта'
    )
    logo = models.ImageField(
        upload_to='image/',
        verbose_name='Лого сайта'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Настройка сайта'
        verbose_name_plural = 'Настройки сайта'

class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Описание о нас'
    )
    descriptions = models.TextField(
        verbose_name='Описание о нас'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фото о нас'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

class Blog(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Названия курса'
    )
    descriptions = models.TextField(
        verbose_name='Описание курса'
    )
    image = models.ImageField(
        upload_to='image/', 
        verbose_name='Фото курса'
    )