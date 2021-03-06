# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Email(models.Model):
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email
