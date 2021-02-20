from django.db import models


class RoomModel(models.Model):
    ROOM_TYPES = (
        ('KS', 'King'),
    )
    id = models.AutoField(primary_key=True)
    room_Type = models.CharField(choices=ROOM_TYPES, max_length=10)


class BookingModel(models.Model):
    id = models.IntegerField(primary_key=True)
    from_Date = models.DateField()
    to_date = models.DateField()
    number_of_rooms = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.from_Date} to {self.to_date} {self.price}"

    class Meta:
        db_table = 'Bookings'
        ordering = ['from_Date']
