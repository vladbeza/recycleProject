from django.contrib import admin
from .models import *

class CommentsInline(admin.StackedInline):
    model = Comment

class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "image", "short_image", "pub_date", "text", "author"]
    list_filter = ["pub_date", "author"]
    inlines = [CommentsInline]

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["nick_name", ]

admin.site.register(NewPost, NewsAdmin)
admin.site.register(Author, AuthorAdmin)