from django.contrib import admin
from mysite.models import Post,Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','text']
admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','author','text']
admin.site.register(Comment,CommentAdmin)
