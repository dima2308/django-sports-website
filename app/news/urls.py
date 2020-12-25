from django.urls import path

from .views import CreateNews, HomeNews, ViewNewsItem, ViewNewsOfCategory

urlpatterns = [
    path('', HomeNews.as_view(), name='index'),
    path('news/<int:pk>/', ViewNewsItem.as_view(), name='view_news_item'),
    path('news/category/<int:category_id>/',
         ViewNewsOfCategory.as_view(), name='view_category_news'),
    path('news/create/', CreateNews.as_view(), name='create_news')
]
