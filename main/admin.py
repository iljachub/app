from django.contrib import admin

from goods.models import categories, Products

admin.site.register(categories)
admin.site.register(Products)