from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import News
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class NewsContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.page_title
        context['btn_text'] = self.btn_text if hasattr(self, 'btn_text') else ''
        return context


class ShowNews(ListView, NewsContextMixin):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']
    page_title = 'STRONA GŁÓWNA'
    paginate_by = 2


class UserShowAllNews(ListView, NewsContextMixin):
    model = News
    template_name = 'blog/user_articles.html'
    context_object_name = 'news'
    page_title = 'ARTYKUŁY UŻYTKOWNIKA'
    paginate_by = 5

    def get_queryset(self): 
        user =get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(avtor=user).order_by('-date')


class ArticleView(DetailView, NewsContextMixin):
    model = News

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = News.objects.get(pk=self.kwargs['pk'])
        return context


class FormMixin(LoginRequiredMixin, UserPassesTestMixin, NewsContextMixin):
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)


class FormatingNews:
    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
     
        return False


class CreateNews(FormMixin, CreateView):
    model = News
    page_title = 'DODAJ NOWY ARTYKUŁ'
    btn_text = 'Opublikuj artykuł'

    def test_func(self):
        return True


class UpdateNews(FormatingNews, FormMixin, UpdateView):
    model = News
    page_title = 'ZAKTUALIZUJ ARTYKUŁ'
    btn_text = 'Opublikuj zmiany'
    
    


class DeleteNews(FormatingNews, LoginRequiredMixin, UserPassesTestMixin, DeleteView, NewsContextMixin):
    model =News
    success_url = '/'
    template_name = 'blog/delete-article.html'
    page_title = 'USUŃ ARTYKUŁ'
    btn_text = 'Usuń'



def abt(request):
    return render(request, 'blog/abt.html', {'title': 'PAGE ABOUT US'})