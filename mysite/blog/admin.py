from django.contrib import admin
from .models import Tag, Category, Post, Comment, Evaluate, Page
# Register your models here.

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Evaluate)
admin.site.register(Page)




