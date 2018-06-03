# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from basicarticle.models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	search_fields = ['none']

admin.site.register(Article,ArticleAdmin)