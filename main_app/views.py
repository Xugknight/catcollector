from django.shortcuts import render
# temporary baby step
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return render(request, 'about.html')