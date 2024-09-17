from django.core.management.base import BaseCommand
from clocks.models import City

class Command(BaseCommand):
    help = 'Populate initial cities'

    def handle(self, *args, **kwargs):
        cities = [
            {'name': 'Los Angeles', 'time_zone': 'America/Los_Angeles'},
            {'name': 'New York', 'time_zone': 'America/New_York'},
            {'name': 'London', 'time_zone': 'Europe/London'},
            {'name': 'Dubai', 'time_zone': 'Asia/Dubai'},
            {'name': 'Bangalore', 'time_zone': 'Asia/Kolkata'},
            {'name': 'Singapore', 'time_zone': 'Asia/Singapore'},
            {'name': 'Tokyo', 'time_zone': 'Asia/Tokyo'},
            {'name': 'Sydney', 'time_zone': 'Australia/Sydney'},
        ]

        for city in cities:
            City.objects.get_or_create(name=city['name'], defaults={'time_zone': city['time_zone']})

        self.stdout.write(self.style.SUCCESS('Successfully populated cities'))
