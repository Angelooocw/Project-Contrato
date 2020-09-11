from django.contrib import admin
from .models import Category, Content


class ContentAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_filter = ('category',)
    filter_horizontal = ()


admin.site.register(Content, ContentAdmin)
admin.site.register(Category)
