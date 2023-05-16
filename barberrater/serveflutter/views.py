from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

def serve_flutter_app(request):
    return HttpResponse("Hello, world. flutter index call here")

