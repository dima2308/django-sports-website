from .views import create_news, index, view_category_news, view_news_item
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('news/<int:news_item_id>/', view_news_item, name='view_news_item'),
    path('news/category/<int:category_id>/', view_category_news, name='view_category_news'),
    path('news/create/', create_news, name='create_news')
]
