from rest_framework import serializers

from lookups import models


class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Spell
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'
