#-*- codin:utf-8 -*-
from django.db import models

from __future__ import unicode_literals#추가 파이썬2 지원
from django.utils.encoding import python_2_unicode_compatible#추가

# Create your models here.
@python_2_unicode_compatible#추가
class Bookmark(models.Model):#추가
    title=models.CharField(max_legth=100, blank=True, null=True)
    url=models.URLField('url',unipue=True)
    
    def __str__(self):
        return self.title