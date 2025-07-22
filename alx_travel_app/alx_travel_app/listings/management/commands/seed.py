from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings (no Faker)'

    def handle(self, *args, **kwargs):
        # Check or create a default user
        user, created = User.objects.get_or_create(username='demo_user')
        if created:
            user.set_password('password123')
            user.save()
            self.stdout.write(self.style.WARNING('Created default user: demo_user'))

        # Clear old listings
        Listing.objects.all().delete()

        # Sample data
        sample_titles = [
            "Cozy Apartment in the City",
            "Beachfront Villa Retreat",
            "Modern Studio Downtown",
            "Spacious Countryside House",
            "Charming Mountain Cabin",
        ]

        sample_descriptions = [
            "A lovely place to relax and unwind.",
            "Perfect for a weekend getaway!",
            "Close to public transport and shops.",
            "Quiet area, great for families.",
            "Stunning views and fresh air guaranteed.",
        ]

        sample_locations = ["Ibadan", "Lagos", "Abuja", "Osogbo", "Abeokuta"]

        # Create 10 listings
        for i in range(10):
            Listing.objects.create(
                owner=user,
                title=random.choice(sample_titles),
                description=random.choice(sample_descriptions),
                location=random.choice(sample_locations),
                price_per_night=round(random.uniform(50, 200), 2),
                available=random.choice([True, False]),
            )

        self.stdout.write(self.style.SUCCESS('✅ Successfully seeded 10 listings without using Faker.'))
