from django.db import models


class Thing(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(
        unique=True,
        max_length=255,
        null=False,
        blank=False,
        default=None,
        help_text="The abstract parent class for all reference lookup types"
    )

    short_description = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default=None,
        help_text="A roughly one-breath sentence that describes the thing"
    )

    full_description = models.TextField(
        null=True,
        blank=True,
        default=None,
        help_text="The full description of what the thing is"
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
