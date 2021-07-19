from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import News
from .forms import AddNewsForm
from django.utils import timezone

class NewsList(LoginRequiredMixin, ListView):
    model = News
    context_object_name = 'news_list'
    template_name = 'news/news_list.html' 

class NewsDetailView(LoginRequiredMixin, DetailView):
    model = News

@login_required()
def index(request):
    num_news = News.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_news':num_news}
    )

@login_required()
def add_news(request):
    if request.method == 'POST':
        form = AddNewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author_id = request.user
            news.create_on = timezone.now()
            news.save()
            return redirect('news-detail', pk=news.pk)
    else:
        form = AddNewsForm()
    return render(
        request,
        'news/add_news.html',
        {'form':form}
    )