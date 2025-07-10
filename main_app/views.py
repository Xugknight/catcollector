from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Cat, Toy
from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    # toys = Toy.objects.all()  # Fetch all toys
    # Obtain list of toys ids that the cat has
    toys_cat_has = cat.toys.all().values_list('id')
    # Query for toys that the cat doesn't have
    toys = Toy.objects.exclude(id__in=toys_cat_has)
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        'cat': cat, 
        'toys': toys,  # Pass toys to the template
        'feeding_form': feeding_form
        })

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    # success_url = '/cats/{id}' one way to redirect to the newly created cat's page

class CatUpdate(UpdateView):
    model = Cat
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'

def add_feeding(request, cat_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('cat-detail', cat_id=cat_id)

class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'breed', 'description', 'age']

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

def associate_toy(request, cat_id, toy_id):
    # Note that you can pass a toy's id instead of the whole object
    Cat.objects.get(id=cat_id).toys.add(toy_id) # Does it all on one line
    # cat = Cat.objects.get(id__exact=cat_id)
    # cat.toys.add(toy_id)
    return redirect('cat-detail', cat_id=cat_id)