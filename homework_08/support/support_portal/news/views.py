from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import News

class NewsList(ListView):
    model = News
    context_object_name = 'news_list'
    template_name = 'news/news_list.html' 

class NewsDetailView(DetailView):
    model = News


def index(request):
    num_news = News.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_news':num_news}
    )