from django.contrib import admin
from .models import Post, Comment, Hashtag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['content',]
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content',]
admin.site.register(Comment, CommentAdmin)

class HashtagAdmin(admin.ModelAdmin):
    list_display = ['content',]
admin.site.register(Hashtag, HashtagAdmin)