from django.db import models
from django.db.models.base import Model
from django.urls import reverse


class News(models.Model):
    title = models.CharField('Заголовок', max_length=150, unique=True)
    content = models.TextField('Содержимое')
    photo = models.URLField('Фотография')
    category = models.ForeignKey(
        'Category', verbose_name='Категория', on_delete=models.PROTECT)
    is_published = models.BooleanField('Опубликовано', default=True)
    views = models.IntegerField('Количество просмотров', default=0)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    edited_at = models.DateTimeField('Дата редактирования', auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("view_news_item", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField('Название', max_length=150, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("view_category_news", kwargs={"category_id": self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
