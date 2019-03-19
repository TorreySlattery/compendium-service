from rest_framework import serializers

from lookups import models


class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Spell
        fields = '__all__'
