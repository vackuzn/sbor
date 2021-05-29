from django.contrib import admin
from main.models import *
from django.utils.safestring import mark_safe


class GlobalCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'views', 'photo', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_editable = ('is_published',)

    fields = ('title', 'is_published', 'views', 'slug', 'photo', 'get_photo')
    readonly_fields = ('views', 'get_photo')

    def get_photo(self, obj):
        if obj.photo:
            res = mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            res = "нет картинки"
        return res

    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'global_category', 'is_published', 'views', 'photo', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_editable = ('is_published', 'global_category')

    fields = ('title', 'is_published', 'global_category', 'views', 'slug', 'photo', 'get_photo')
    readonly_fields = ('views', 'get_photo')

    def get_photo(self, obj):
        if obj.photo:
            res = mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            res = "нет картинки"
        return res

    get_photo.short_description = 'Миниатюра'


class ImageGalleryInline(admin.TabularInline):
    model = ImageGallery
    extra = 1
    fields = ('additional_picture', 'created_at', 'get_photo')
    readonly_fields = ('get_photo', 'created_at')

    def get_photo(self, obj):
        if obj.additional_picture:
            res = mark_safe(f'<img src="{obj.additional_picture.url}" width="75">')
        else:
            res = "нет картинки"
        return res

    get_photo.short_description = 'Доп. картинка'


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageGalleryInline, ]
    list_display = ('get_photo', 'title', 'article', 'is_published', 'category', 'price_unit', 'views')
    list_display_links = ('title', 'article')
    search_fields = ('title', 'article', 'category')
    list_editable = ('price_unit', 'is_published')
    fields = ('get_photo', 'main_image', 'title', 'article', 'category', 'is_published', 'description', 'price_unit',
              'views', 'created_at', 'update_at')
    readonly_fields = ('get_photo', 'created_at', 'update_at', 'views')

    def get_photo(self, obj):
        if obj.main_image:
            res = mark_safe(f'<img src="{obj.main_image.url}" width="75">')
        else:
            res = "нет картинки"
        return res

    get_photo.short_description = 'Фото'


admin.site.register(GlobalCategory, GlobalCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.site_title = "Админ панель"
admin.site.site_header = "Админ панель"
