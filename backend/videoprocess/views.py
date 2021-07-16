from django.shortcuts import render

# Create your views here.
from .models import Address

def address_view(request):
    address = Address.objects.all()
    return address
    # return render(request, {"address": address})