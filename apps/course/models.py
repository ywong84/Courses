from __future__ import unicode_literals

from django.db import models

# Create your models here.
class course(models.Model):
    course_name = models.CharField(max_length=45)
    description = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
