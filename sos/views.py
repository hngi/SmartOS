from django.shortcuts import render

# Create your views here.
def sos(request):
    return render(request, 'sos.html', {})