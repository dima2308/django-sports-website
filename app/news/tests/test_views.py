from django.test import TestCase
from django.urls import reverse
from news.models import News, Category


class NewsViewsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        num_of_news = 4
        category = Category.objects.create(title='Тестовая категория')
        for num in range(num_of_news):
            News.objects.create(title=f'Тестовая новость{num}',
                                content=f'Контент{num}', category=category)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'news/index.html')

    def test_pagination(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['news']) == 2)
