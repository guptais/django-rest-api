from django.contrib import admin
from django.urls import path, include
from .views import BookingsView, BookingView

urlpatterns = [
    path('', BookingsView),
    path('booking/<int:nm>', BookingView),
]
