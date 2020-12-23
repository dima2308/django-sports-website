from .models import Category, News
from django.contrib import admin


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published',
                    'created_at', 'edited_at')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category)
