from django.shortcuts import render, HttpResponseRedirect, Http404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import BookingModel, RoomModel
from .serializers import BookingSerializer


@csrf_exempt
def BookingsView(request):

    if request.method == 'GET':
        bookings = BookingModel.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.Method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookingSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def BookingView(request, nm):
    try:
        booking = BookingModel.objects.get(id=nm)
    except:
        raise Http404("Not Found")

    if request.method == 'GET':
        serializer = BookingSerializer(booking)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BookingSerializer(booking, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    if request.method == 'DELETE':
        booking.delete()
        return HttpResponse(status=204)
