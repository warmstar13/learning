from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're in the polls index.")
