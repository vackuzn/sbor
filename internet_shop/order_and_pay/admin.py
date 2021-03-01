from django.contrib import admin
from order_and_pay.models import Order, OrderProduct
from django.utils.safestring import mark_safe


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1
    fields = ('get_photo', 'product', 'price', 'quantity')
    readonly_fields = ('get_photo', 'product', 'price')

    def get_photo(self, obj):
        if obj.product.main_image:
            res = mark_safe(f'<img src="{obj.product.main_image.url}" width="75">')
        else:
            res = "нет картинки"
        return res

    get_photo.short_description = 'Изображение'


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline, ]
    list_display = ('order_number', 'first_name', 'last_name', 'phone', 'address', 'created', 'total_price', 'status')
    list_display_links = ('order_number',)
    list_editable = ('status',)
    fields = ('order_number', 'user', 'first_name', 'last_name', 'phone', 'email', 'city', 'address', 'created', 'total_price', 'status')

    readonly_fields = ('user', 'created')


admin.site.register(Order, OrderAdmin)




