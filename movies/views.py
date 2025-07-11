from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import Movie
from .forms import MovieForm

def index(request):
    movies = Movie.objects.order_by('title')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'movies': movies}, request))
    
def movie_details(request, id: int):
    movie = Movie.objects.get(pk=id)
    template = loader.get_template('movie_details.html')
    context = {
        'movie': movie
    }
    return HttpResponse(template.render(context, request))
    
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
        
    else:
        form = MovieForm()
            
    return render (request, 'movie_form.html', {'form': form})