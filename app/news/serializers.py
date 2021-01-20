from rest_framework import serializers
from .models import Category, News


class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    content = serializers.CharField()
    photo = serializers.URLField()
    category = serializers.CharField()
    is_published = serializers.BooleanField()
    views = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    edited_at = serializers.DateTimeField()

    def create(self, validated_data):
        return News.objects.create(**validated_data)