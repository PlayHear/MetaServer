#Author - Shivam Kapoor
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

#Creating user_data model to store data.
class user_data(models.Model):
    User_name = models.CharField(max_length=200)
    Full_name = models.CharField(max_length=250, blank=True, null=True)

    class Meta(object):
        verbose_name = '1_User Data'
        verbose_name_plural = '1_User Data'

    def __unicode__(self): #Python2 declaration
        return (str(self.Full_name + str(self.Idx)))