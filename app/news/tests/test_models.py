from django.db.utils import IntegrityError
from django.test import TestCase
from news.models import Category, News


class NewsModelTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(title='Тестовая категория')
        News.objects.create(title='Тестовая новость',
                            content='Контент', category=category)

    def setUp(self):
        self.category = Category.objects.get(pk=1)
        self.item = News.objects.get(pk=1)

    def test_create_existed_news(self):
        try:
            News.objects.create(title='Тестовая новость',
                                content='Контент', category=self.category)
        except IntegrityError:
            self.assertRaisesMessage(
                IntegrityError, 'UNIQUE constraint failed: news_news.title')

    def test_max_length_title_news(self):
        max_length = self.item._meta.get_field('title').max_length
        self.assertEquals(max_length, 150)

    def test_default_count_views(self):
        views = self.item.views
        self.assertEquals(views, 0)

    def test_default_is_published(self):
        is_published = self.item.is_published
        self.assertEquals(is_published, True)

    def test_get_str_news(self):
        self.assertEquals(self.item.__str__(), 'Тестовая новость')

    def test_get_absolute_url(self):
        item = News.objects.get(pk=1)
        self.assertEquals(item.get_absolute_url(), '/news/1/')


class CategoryModelTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(title='Тест')

    def setUp(self):
        self.category = Category.objects.get(pk=1)

    def test_create_existed_category(self):
        try:
            Category.objects.create(title='Тест')
        except IntegrityError:
            self.assertRaisesMessage(
                IntegrityError, 'UNIQUE constraint failed: category_category.title')

    def test_get_str_category(self):
        self.assertEquals(self.category.__str__(), 'Тест')
