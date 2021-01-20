from django.db.models.query_utils import select_related_descend
from rest_framework import serializers
from .models import Category, News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'content', 'category', 'photo',
                  'is_published', 'views', 'created_at']
