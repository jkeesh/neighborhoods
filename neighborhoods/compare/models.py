# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class CityComparison(models.Model):
    """A model to save a single city/neighborhood comparison."""

    start_city = models.CharField(max_length=200)
    neighborhood1 = models.CharField(max_length=200)

    end_city = models.CharField(max_length=200)
    neighborhood2 = models.CharField(max_length=200)

    timestamp = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.start_city + ":" + self.neighborhood1 + ", " \
        + self.end_city + ":" + self.neighborhood2 + " (" + self.username + ")"
