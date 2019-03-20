from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from lookups import models

from api import serializers


class SpellViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Spell.objects.all()
    serializer_class = serializers.SpellSerializer

    def filter_queryset(self, queryset):
        return queryset

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs['pk']
        try:
            obj = models.Spell.objects.get(pk=pk)
        except models.Spell.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.SpellSerializer(obj, context={'request': request})
        return Response(serializer.data)


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs['pk']
        try:
            obj = models.Item.objects.get(pk=pk)
        except models.Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.ItemSerializer(obj, context={'request': request})
        return Response(serializer.data)
