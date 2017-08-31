#-*- coding:utf-8 -*-
from django.contrib import admin

from bookmark.models import Bookmark#추가

# Register your models here.

class BookmarkAdmin(admin.ModelAdmin):#추가
    list_display=('title', 'url')
    
admin.site.register(Bookmark, BookmarkAdmin)