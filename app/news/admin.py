from .models import Category, News
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(label='Содержимое', widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('title', 'category', 'is_published',
                    'created_at', 'edited_at')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'category')
    fields = ('title', 'category', 'content', 'views',
              'created_at', 'edited_at', 'is_published')
    readonly_fields = ('views', 'created_at', 'edited_at')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category)

admin.site.site_title = 'Панель управления'
admin.site.site_header = 'Панель управления'
