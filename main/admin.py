from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_at')
    list_filter = ('title', 'create_at')
admin.site.register(Category, CategoryAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'create_at', 'price')
    list_filter = ('category', 'create_at', 'price')
admin.site.register(Book, BookAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category','price', 'create_at')
    list_filter = ('category', 'price', 'name')
admin.site.register(Product, ProductAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'create_at')
    list_filter = ('cart_id', 'create_at')
admin.site.register(Cart, CartAdmin)