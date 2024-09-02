from enum import unique

from django.db import models

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Текст')
    title2 = models.CharField('Заголовок1', max_length=50)
    text2 = models.TextField('Текст2')
    title3 = models.CharField('Заголовок3', max_length=50)
    text3 = models.TextField('Текст3')

