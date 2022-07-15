# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.conf import settings

# Create your models here.

class adminuser(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
    )

    class Meta:
        permissions = (
            ('can_use_admin','Can Use Admin'),

        )