# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
# from django.conf import settings
# from django.core.validators import MinValueValidator, MaxValueValidator
#
# # Create your models here.
#
# class adminuser(models.Model):
#     class Meta:
#         permissions = (
#             ('can_use_admin','Can Use Admin'),
#
#         )
#
#
# class normaluser(models.Model):
#     id = models.PositiveIntegerField(primary_key=True)
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         default=1,
#     )
#
#     correct_counts = models.PositiveIntegerField(null=False,blank=False,default=0)
#     mistake_counts = models.PositiveIntegerField(null=False,blank=False,default=0)
#
#     class Meta:
#         permissions = (
#             ('can_use_normal','Can Use Normal'),
#
#         )
#
#
#     def __str__(self):
#         return f'{self.author}'
#
#
#     def set_correct_counts(self,counts):
#         self.correct_counts = counts
#         return None
#
#     def add_correct_counts(self):
#         self.correct_counts = self.correct_counts + 1
#         return None
#
#     def get_correct_counts(self):
#         return self.correct_counts
#
#     def set_mistake_counts(self,counts):
#         self.mistake_counts = counts
#         return None
#
#     def add_mistake_counts(self):
#         self.mistake_counts = self.mistake_counts + 1
#         return None
#
#     def get_mistake_counts(self):
#         return self.mistake_counts

