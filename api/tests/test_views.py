from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from django.urls import reverse

from lookups import models


class ThingGetEndpointTestCase:
    """A base set of test cases """
    def setUp(self):
        raise NotImplementedError()

    def _detail_url(self, pk):
        raise NotImplementedError()

    @property
    def objs(self):
        raise NotImplementedError()

    def test_list_exists(self):
        """Should return a 200 on the list endpoint"""
        response = self.client.get(self.list_url)
        assert response.status_code == status.HTTP_200_OK

    def test_list_returns_items(self):
        """Should return a list of existing items"""
        response = self.client.get(self.list_url)
        assert len(response.data) == 5

    def test_detail_exists(self):
        """Should return a 200 on the retrieve endpoint"""
        pk = self.objs.first().pk
        response = self.client.get(self._detail_url(pk))
        assert response.status_code == status.HTTP_200_OK

    def test_detail_returns_item(self):
        """Should return a single item on the retrieve endpoint"""
        pk = self.objs.first().pk
        response = self.client.get(self._detail_url(pk))
        assert response.data['id'] == pk

    def test_detail_404(self):
        """Should return a 404 on the retrieve endpoint if the pk doesn't exist"""
        response = self.client.get(self._detail_url('9000'))
        assert response.status_code == status.HTTP_404_NOT_FOUND


class SpellGetEndpointTestCase(ThingGetEndpointTestCase, APITestCase):
    def setUp(self):
        self.list_url = reverse('spell-list')
        spells = []
        for name in ['Lightning Bolt', 'Fireball', 'Ice Nova', 'Blink', 'Serenity']:
            spells.append(models.Spell(name=name, range=120))
        models.Spell.objects.bulk_create(spells)

    @property
    def objs(self):
        return models.Spell.objects.all()

    def _detail_url(self, pk):
        return reverse('spell-detail', kwargs={'pk': pk})


class ItemGetEndpointTestCase(ThingGetEndpointTestCase, APITestCase):
    def setUp(self):
        self.list_url = reverse('item-list')
        items = []
        for name in ['Longsword', 'Bag of Holding', 'Alchemy Kit', "50' of hempen rope", "Rations"]:
            items.append(models.Item(name=name))
        models.Item.objects.bulk_create(items)

    @property
    def objs(self):
        return models.Item.objects.all()

    def _detail_url(self, pk):
        return reverse('item-detail', kwargs={'pk': pk})
