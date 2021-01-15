from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from .forms import NewsForm
from .models import Category, News


class HomeNews(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/index.html'

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
