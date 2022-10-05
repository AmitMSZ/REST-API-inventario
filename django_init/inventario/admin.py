from django.contrib import admin

from inventario.models import Bodega, Products

# Register your models here.

admin.site.register(Products)
admin.site.register(Bodega)
