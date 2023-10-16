from django.contrib import admin

from cats.models import Cat, Achievement


class KittygramAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'birth_year', 'owner', 'image')


admin.site.register(Cat, KittygramAdmin)
admin.site.register(Achievement)
