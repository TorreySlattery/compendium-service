from django.contrib import admin

from lookups import models


class ThingAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description',)
    search_fields = ('name', 'short_description',)


class SpellAdmin(ThingAdmin):
    model = models.Spell


class ItemAdmin(ThingAdmin):
    models = models.Item


admin.site.register(models.Spell, SpellAdmin)
admin.site.register(models.Item, ItemAdmin)
