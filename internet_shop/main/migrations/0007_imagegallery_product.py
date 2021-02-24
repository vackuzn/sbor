# Generated by Django 3.1.6 on 2021-02-18 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210218_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название товара')),
                ('article', models.IntegerField(unique=True, verbose_name='Артикул товара')),
                ('description', models.TextField(blank=True, verbose_name='Описание товара')),
                ('main_image', models.ImageField(blank=True, upload_to='product_photo/', verbose_name='Главное изображение')),
                ('price_unit', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена за штуку')),
                ('price_pack', models.DecimalField(blank=True, decimal_places=2, max_digits=9, verbose_name='Цена за упаковку')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления товара')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления товара')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация (да/нет)')),
                ('views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_picture', models.ImageField(blank=True, upload_to='product_photo/', verbose_name='Дополнительное изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Дополнительное изображение',
                'verbose_name_plural': 'Дополнительные изображения',
                'ordering': ['-created_at'],
            },
        ),
    ]