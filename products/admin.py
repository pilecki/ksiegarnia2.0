from django.contrib import admin
from .models import Product, Category, Genre, Authors, ComingSoon, Formats


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'promotion',
        'rating',
        'image',
        'pub_date',
        'author1',
        'author2',
        'formats',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class AuthorsAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class FormatsAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ComingSoonAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'available_date',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Formats, FormatsAdmin)
admin.site.register(ComingSoon, ComingSoonAdmin)





