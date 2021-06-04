from django.db import models
from django.urls import reverse
from PIL import Image

_MAX_SIZE = 800


class GlobalCategory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, verbose_name='Название категории')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='Слаг')
    photo = models.ImageField(upload_to='category_photos/', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Меняем разрешение картинки на меньшее, если оно больше максимального размера в пикселях.
        """
        super(GlobalCategory, self).save(*args, **kwargs)
        if self.photo:
            filepath = self.photo.path
            width = self.photo.width
            height = self.photo.height

            max_size = max(width, height)

            if max_size > _MAX_SIZE:
                image = Image.open(filepath)
                image = image.resize(
                    (round(width / max_size * _MAX_SIZE),  # Сохраняем пропорции
                     round(height / max_size * _MAX_SIZE)),
                    Image.ANTIALIAS)
                image.save(filepath)

    class Meta:
        verbose_name = "Глобальная категория"
        verbose_name_plural = "Глобальные категории"
        ordering = ['title']


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, verbose_name='Название категории')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='Слаг')
    global_category = models.ForeignKey(GlobalCategory, on_delete=models.CASCADE, verbose_name='Глобальная категория')
    photo = models.ImageField(upload_to='category_photos/', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Меняем разрешение картинки на меньшее, если оно больше максимального размера в пикселях.
        """
        super(Category, self).save(*args, **kwargs)
        if self.photo:
            filepath = self.photo.path
            width = self.photo.width
            height = self.photo.height

            max_size = max(width, height)

            if max_size > _MAX_SIZE:
                image = Image.open(filepath)
                image = image.resize(
                    (round(width / max_size * _MAX_SIZE),  # Сохраняем пропорции
                     round(height / max_size * _MAX_SIZE)),
                    Image.ANTIALIAS)
                image.save(filepath)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']


class Product(models.Model):

    CHOICES_UNIT = [
        ('piece', 'штуку'),
        ('kilogram', 'килограмм'),
        ('gram', 'грамм'),
        ('centimeter', 'сантиметр'),
        ('meter', 'метр'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, verbose_name='Название')
    article = models.IntegerField(verbose_name='Артикул', unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    main_image = models.ImageField(verbose_name='Главное изображение', upload_to='product_photo/', blank=True)
    price_unit = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена за штуку')
    unit_of_measurement = models.CharField(max_length=200,
                                           choices=CHOICES_UNIT, default='piece',
                                           verbose_name='Единица измерения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_card', kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        """
        Меняем разрешение картинки на меньшее, если оно больше максимального размера в пикселях.
        """
        super(Product, self).save(*args, **kwargs)
        if self.main_image:
            filepath = self.main_image.path
            width = self.main_image.width
            height = self.main_image.height

            max_size = max(width, height)

            if max_size > _MAX_SIZE:
                image = Image.open(filepath)
                image = image.resize(
                    (round(width / max_size * _MAX_SIZE),  # Сохраняем пропорции
                     round(height / max_size * _MAX_SIZE)),
                    Image.ANTIALIAS)
                image.save(filepath)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-views']


class ImageGallery(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    additional_picture = models.ImageField(verbose_name='Дополнительное изображение', upload_to='product_photo/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.product.title

    def save(self, *args, **kwargs):
        """
        Меняем разрешение картинки на меньшее, если оно больше максимального размера в пикселях.
        """
        super(ImageGallery, self).save(*args, **kwargs)
        if self.additional_picture:
            filepath = self.additional_picture.path
            width = self.additional_picture.width
            height = self.additional_picture.height

            max_size = max(width, height)

            if max_size > _MAX_SIZE:
                image = Image.open(filepath)
                image = image.resize(
                    (round(width / max_size * _MAX_SIZE),  # Сохраняем пропорции
                     round(height / max_size * _MAX_SIZE)),
                    Image.ANTIALIAS)
                image.save(filepath)

    class Meta:
        verbose_name = "Дополнительное изображение"
        verbose_name_plural = "Дополнительные изображения"
        ordering = ['-created_at']


class Wish(models.Model):
    CHOICES_STATUS = [
        ('wish_is_made', 'Создано'),
        ('wish_is_done', 'Выполнено'),
        ('wish_is_fulfilled', 'Отклонено'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, verbose_name='Краткое описание')
    name = models.CharField(max_length=150, verbose_name='Имя')
    description = models.TextField(verbose_name='Подробное описание', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.CharField(max_length=200, choices=CHOICES_STATUS, default='wish_is_made', verbose_name='Статус')

    class Meta:
        verbose_name = "Пожелание"
        verbose_name_plural = "Пожелания"
        ordering = ['-created_at']


class SiteSettings(models.Model):
    key_title = models.CharField(max_length=150, verbose_name='Ключ')
    description = models.CharField(max_length=150, verbose_name='Описание')
    value = models.TextField(verbose_name='Значение')

    class Meta:
        verbose_name = "Настройка сайта"
        verbose_name_plural = "Настройки сайта"
