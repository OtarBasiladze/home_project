from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_about(request):
    return HttpResponse('About is working')
