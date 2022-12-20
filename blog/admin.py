from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_disply = ('title','date_created','author')

# creat a post add new blogs and users #
admin.site.register(Post,PostAdmin)