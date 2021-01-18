from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView

from .forms import LoginForm, NewsForm, RegisterForm
from .models import Category, News


class HomeNews(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/index.html'
    paginate_by = 2

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class ViewNewsOfCategory(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/category_news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(
            pk=self.kwargs.get('category_id'))
        return context

    def get_queryset(self):
        return News.objects.filter(
            category_id=self.kwargs.get('category_id')
        ).select_related('category')


class ViewNewsItem(DetailView):
    model = News
    context_object_name = 'news_item'
    template_name = 'news/view_news_item.html'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/create_news_form.html'
    raise_exception = True


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрированы!')
            return redirect('index')
        else:
            messages.error(request, 'Заполните корректно все поля!')

    form = RegisterForm()

    return render(request, template_name='news/register.html', context={'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')

    form = LoginForm()

    return render(request, template_name='news/login.html', context={'form': form})


def logout_user(request):
    logout(request)
    return redirect('index')
