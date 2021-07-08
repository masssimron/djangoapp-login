from django.shortcuts import redirect, render
from .models import Authentication
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, "index.html")

