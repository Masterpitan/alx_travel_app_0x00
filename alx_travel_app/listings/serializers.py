from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Listing
        fields = [
            'id',
            'owner',
            'title',
            'description',
            'location',
            'price_per_night',
            'available',
            'created_at',
        ]


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # Display booking user's username
    listing = serializers.PrimaryKeyRelatedField(queryset=Listing.objects.all())

    class Meta:
        model = Booking
        fields = [
            'id',
            'listing',
            'user',
            'check_in',
            'check_out',
            'guests',
            'created_at',
        ]
