from django.shortcuts import render


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


from rest_framework.serializers import ModelSerializer
from .models import *


class SerializeCustomer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class SerializeItem(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"



