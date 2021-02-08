from django.contrib import admin
from main.models import Category
from django.utils.safestring import mark_safe


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'views', 'photo', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_editable = ('is_published',)

    fields = ('title', 'is_published', 'views', 'photo', 'get_photo')
    readonly_fields = ('views', 'get_photo')


    def get_photo(self, obj):
        if obj.photo:
            res = mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            res = "нет картинки"
        return res

    get_photo.short_description = 'Миниатюра'




admin.site.register(Category, CategoryAdmin)

