from django.contrib import admin

from lookups import models


class ThingAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description',)
    search_fields = ('name', 'short_description',)
    ordering = ('name',)


class SpellAdmin(ThingAdmin):
    model = models.Spell
    list_display = ('name', 'is_concentration', 'is_ritual', 'short_description')
    list_filter = ('is_concentration', 'is_ritual',)


class ItemAdmin(ThingAdmin):
    models = models.Item


admin.site.register(models.Spell, SpellAdmin)
admin.site.register(models.Item, ItemAdmin)
