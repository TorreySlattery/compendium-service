from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from django.urls import reverse

from lookups import models


class SpellGetEndpointTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('spell-list')
        spells = []
        for name in ['Lightning Bolt', 'Fireball', 'Ice Nova', 'Blink', 'Serenity']:
            spells.append(models.Spell(name=name, range=120))

        models.Spell.objects.bulk_create(spells)

    def _detail_url(self, pk):
        return reverse('spell-detail', kwargs={'pk': pk})

    def test_list_exists(self):
        """Should return a 200 on the list endpoint"""
        response = self.client.get(self.list_url)
        assert response.status_code == status.HTTP_200_OK

    def test_list_returns_items(self):
        """Should return a list of existing items"""
        response = self.client.get(self.list_url)
        assert len(response.data) == 5
