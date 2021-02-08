from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название категории')
    photo = models.ImageField(upload_to='category_photos/', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']
