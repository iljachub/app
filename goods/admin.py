from django.contrib import admin

from goods.models import categories, Products

# admin.site.register(categories)
# admin.site.register(Products)

@admin.register(categories)
class categoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}       


