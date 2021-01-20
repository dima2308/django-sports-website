from django.db.utils import IntegrityError
from django.test import TestCase
from news.models import Category, News


class NewsModelTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(title='Тестовая категория')
        News.objects.create(title='Тестовая новость',
                            content='Контент', category=category)

    category = Category.objects.get(pk=1)

    def test_create_existed_news(self):
        try:
            News.objects.create(title='Тестовая новость',
                                content='Контент', category=self.category)
        except IntegrityError:
            self.assertRaisesMessage(
                IntegrityError, 'UNIQUE constraint failed: news_news.title')

    def test_max_length_title_news(self):
        item = News.objects.get(pk=1)
        max_length = item._meta.get_field('title').max_length
        self.assertEquals(max_length, 150)

    def test_default_count_views(self):
        item = News.objects.get(pk=1)
        views = item.views
        self.assertEquals(views, 0)

    def test_default_is_published(self):
        item = News.objects.get(pk=1)
        is_published = item.is_published
        self.assertEquals(is_published, True)

    def test_get_absolute_url(self):
        item = News.objects.get(pk=1)
        self.assertEquals(item.get_absolute_url(), '/news/1/')
