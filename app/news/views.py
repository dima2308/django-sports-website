from .forms import NewsForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, News


def index(request):
    news = News.objects.filter(is_published=True)
    context = {
        'news': news
    }
    return render(request, 'news/index.html', context)


def view_category_news(request, category_id):
    category_news = News.objects.filter(category=category_id)
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'news': category_news,
        'category': category
    }
    return render(request, 'news/category_news.html', context)


def view_news_item(request, news_item_id):
    news_item = get_object_or_404(News, pk=news_item_id)
    context = {
        'news_item': news_item
    }
    return render(request, 'news/view_news_item.html', context)


def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)

    form = NewsForm()
    return render(request, 'news/create_news_form.html', {'form': form})
