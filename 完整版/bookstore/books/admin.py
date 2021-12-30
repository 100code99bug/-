from django.contrib import admin
from . import models
# Register your models here.

class BookManager(admin.ModelAdmin):
    list_display = ['id','btitle','bread','bcomment','is_delete']
admin.site.register(models.Book, BookManager)