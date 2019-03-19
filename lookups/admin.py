from django.contrib import admin

from lookups import models


class SpellAdmin(admin.ModelAdmin):
    model = models.Spell

    list_display = ('name', 'short_description',)
    search_fields = ('name', 'short_description',)


admin.site.register(models.Spell, SpellAdmin)
