from __future__ import unicode_literals  
from django.db import models
from django.forms import ModelForm

class Bugs(models.Model):
    description = models.CharField(max_length=200)
    bug_type = models.CharField(max_length=20)
    report_date = models.DateTimeField("date reported")
    status = models.CharField(max_length=30)


