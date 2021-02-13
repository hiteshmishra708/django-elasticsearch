# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.http import JsonResponse

class Supplier(models.Model):
    name = models.CharField(max_length=30)

    class Meta(object):
        """Meta options."""

        ordering = ["id"]

    def __str__(self):
        return '%s' % (self.name)

class Category(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=100, blank=True)

    class Meta(object):
        """Meta options."""

        ordering = ["id"]

    def __str__(self):
        return '%s' % (self.name)

class Product(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=100, blank=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, unique=False, null=True)
    supplied_by = models.ForeignKey(Supplier, on_delete=models.CASCADE, unique=False, null=True)

    class Meta(object):
        """Meta options."""

        ordering = ["id"]

    def __str__(self):
        return '%s | %s' % (self.name, self.cat.name)

    def get_obj(self):
        return {
            'name': self.name,
            'desc': self.desc,
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