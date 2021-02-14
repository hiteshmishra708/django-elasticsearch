# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.http import JsonResponse

class Supplier(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % (self.name)

class Category(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '%s' % (self.name)

class Product(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, unique=False, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, unique=False, null=True)

    def __str__(self):
        return '%s | %s' % (self.name, self.cat.name)

    def get_obj(self):
        return {
            'name': self.name,
            'desc': self.desc,
            'category_desc': self.category.desc,
            'category': self.category.name,
            'supplier': self.supplier.name
        }

class Response():
    def __init__(self, data, status_code=200, message=None):
        self.data = data
        self.status_code = status_code
        self.message = message

    def get_obj(self):
        return JsonResponse({
            'status_code': self.status_code,
            'data': self.data,
            'message': self.message,
        })