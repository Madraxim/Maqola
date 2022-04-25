from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import ArticleForm, LoginForm, RegistrationForm
from .models import Article, Category



class ArticleList(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = 'articles'
    extra_context = {
        'title': "Maqolalar"
    }
    paginate_by = 2
    def get_queryset(self):
        return Article.objects.filter(published=True).select_related('category')



class ArticleDetail(LoginRequiredMixin, DetailView):
    model = Article

    def get_queryset(self):
        return Article.objects.filter(pk=self.kwargs['pk'], published=True)

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data()
        context['title'] = Article.objects.get(pk=self.kwargs['pk']).title
        return context


class ArticleListByCategory(ArticleList):
    def get_queryset(self):
        return Article.objects.filter(category_id=self.kwargs['pk'], published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = Category.objects.get(pk=self.kwargs['pk']).title
        return context


class SearchResults(ArticleList):
    def get_queryset(self):
        world = self.request.GET.get('q')
        articles = Article.objects.filter(title__icontains=world)
        return articles


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('index')


class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('index')

@login_required()
def profile(request):
    context = {
        'title': 'Sizning profilingiz'
    }
    return render(request, 'blog/profile.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Xush kelibsiz!')
            next = request.POST.get('next', 'index')
            return redirect(next)
    else:
        form = LoginForm()

    context = {
        'title': 'Avtorizatsiya',
        'form': form
    }
    return render(request, 'blog/user_login.html', context)


def user_logout(request):
    logout(request)
    messages.warning(request, 'Siz saytdan chiqdingiz!')
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akkaunt muvaffaqiyatli ochildi!')
            return redirect('login')
        else:
            messages.error(request, 'Registratsiyada xatolik!!!')
    else:
        form = RegistrationForm()
    context = {
        'title': 'Akkaunt ochish',
        'form': form
    }
    return render(request, 'blog/register.html', context)



@login_required()
def new_article(request):
    if request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(**form.cleaned_data)
            article.save()
            return redirect('article_details', article.pk)
    else:
        form = ArticleForm()
    context = {
        'title': "Maqola qo'shish",
        'form': form
    }
    return render(request, 'blog/article_form.html', context)
