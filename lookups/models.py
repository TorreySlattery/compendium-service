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


class Item(Thing):
    type = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default=None,
        help_text="A classification for grouping like items together, e.g. weapons or kits or glasses"
    )

    rarity = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default='Common',
        help_text="The tier of rarity assigned to this item"
    )

    requires_attunment = models.BooleanField(
        default=False,
        help_text="Whether the item requires attunement before it can be fully utilized"
    )

    weight = models.FloatField(
        null=False,
        blank=True,
        default=0.0,
        help_text="The numeric weight of the item (in whatever units you care to use)"
    )

    weight_units = models.CharField(
        max_length=255,
        null=False,
        blank=True,
        default='pounds',
        help_text="The default unit associated with the item's weight"
    )
