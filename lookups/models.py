from django.db import models


class Thing(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default=None,
        help_text="The abstract parent class for all reference lookup types"
    )

    def __str__(self):
        return self.name


class Spell(Thing):
    range = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default=None,
        help_text="The description of how far from the origin the spell can affect things"
    )
