from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CutLink(models.Model):
    descriptions = models.CharField(verbose_name='Введите описание', max_length=255, default='Что то длинное...')
    long_link = models.CharField(verbose_name='Введите ссылку', max_length=255)
    short_link = models.CharField(verbose_name='Коротко о главном', max_length=20)
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return f'{self.descriptions}'

    class Meta:
        verbose_name = 'Ссылку'
        verbose_name_plural = 'Ссылки'