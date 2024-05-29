from django.contrib import admin
from .models import Article, Category, UserArticle

admin.site.register(UserArticle)
admin.site.register(Article)
admin.site.register(Category)

# Register your models here.
