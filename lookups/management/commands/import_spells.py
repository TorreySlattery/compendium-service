import json

from django.core.management.base import BaseCommand
from django.db import transaction, DatabaseError

from lookups import models


class Command(BaseCommand):
    help = "Ingest Spell data from a .json file"

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        with open(options['path'], mode='r') as json_file:
            data = json.load(json_file)
            for name, details in data.items():
                try:
                    with transaction.atomic():
                        defaults = {
                            "full_description": details.get("description", ""),
                            "range": details.get('range', ''),
                            "components": details.get("components", ''),
                            "cast_time": details.get("casting_time", ""),
                            "duration": details.get("duration", ''),
                            "is_concentration": "concentration" in details.get("duration", '').lower(),
                            "is_ritual": "ritual" in details.get('cast_time', '').lower(),
                            "school": details.get("school", ""),
                        }
                        models.Spell.objects.update_or_create(name=name, defaults=defaults)
                except DatabaseError as e:
                    print(e)
