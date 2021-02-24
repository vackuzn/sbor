from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название категории')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='Слаг')
    photo = models.ImageField(upload_to='category_photos/', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    article = models.IntegerField(verbose_name='Артикул', unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    main_image = models.ImageField(verbose_name='Главное изображение', upload_to='product_photo/', blank=True)
    price_unit = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена за штуку')
    price_pack = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена за упаковку', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-views']


class ImageGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    additional_picture = models.ImageField(verbose_name='Дополнительное изображение', upload_to='product_photo/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "Дополнительное изображение"
        verbose_name_plural = "Дополнительные изображения"
        ordering = ['-created_at']

