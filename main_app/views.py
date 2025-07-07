from django.shortcuts import render

# Create your views here.
def home(request):
    # return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cat_index(request):
    # Render the cats/index.html template with the cats data
    return render(request, 'cats/index.html', {'cats': cats})