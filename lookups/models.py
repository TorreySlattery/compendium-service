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

    source = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default=None,
        help_text="If applicable, the original source for this"
    )

    def __str__(self):
        return "({}) {}".format(self.__class__.__name__, self.name)


class Spell(Thing):
    range = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default=None,
        help_text="The description of how far from the origin the spell can affect things"
    )

    components = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default=None,
        help_text="Whatever spell components are necessary to cast the spell"
    )

    cast_time = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default=None,
        help_text="How long it takes to cast the spell"
    )

    is_concentration = models.BooleanField(
        default=False,
        help_text="Whether the spell requires concentration or not"
    )

    is_ritual = models.BooleanField(
        default=False,
        help_text="Whether the spell can be cast as a ritual or not"
    )

    school = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default=None,
        help_text="What spell school this belongs to, e.g. evocation or conjuration"
    )
