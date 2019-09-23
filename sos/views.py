from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h3> SmartOS's sample website </h3>\n<p>Trying out web development with django, such a fancy-looking site.</p>")