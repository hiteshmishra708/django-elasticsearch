# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Supplier, Category, Product

admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Product)
