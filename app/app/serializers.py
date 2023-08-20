from rest_framework import serializers
from .models import User, PaymentMethod, Seat, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'password_hash', 'email', 'full_name', 'profile_photo_link']

class PaySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['payment_id', 'user_id', 'card_number', 'card_expiry']

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['seat_id', 'spaceship_id', 'availability', 'booking_id']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'booking_id', 'user_id', 'schedule_id',
            'num_passengers', 'starting_planet', 'destination',
            'departure_date', 'spaceship_name', 'spaceship_company'
        ]
