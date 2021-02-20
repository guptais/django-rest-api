from rest_framework import serializers
from .models import BookingModel, RoomModel


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
        fields = ['id', 'from_Date', 'to_date', 'number_of_rooms', 'price']
