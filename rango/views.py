from django.shortcuts import render


# Create your views here.

def index(request):
    response = render(request, 'wwworkout/index.html')
    return response
