from django.urls import path

from .views import (CreateNews, HomeNews, NewsView, SingleNewsView, ViewNewsItem, ViewNewsOfCategory, contact_us,
                    login_user, logout_user, register_user)

urlpatterns = [
    path('', HomeNews.as_view(), name='index'),
    path('news/<int:pk>/', ViewNewsItem.as_view(), name='view_news_item'),
    path('news/category/<int:category_id>/',
         ViewNewsOfCategory.as_view(), name='view_category_news'),
    path('news/create/', CreateNews.as_view(), name='create_news'),
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('contact/', contact_us, name='contact_us'),
    path('api/<int:pk>', SingleNewsView.as_view()),
    path('api/', NewsView.as_view())
]
