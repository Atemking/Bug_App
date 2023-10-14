from __future__ import unicode_literals  
from django.db import models
from django.forms import ModelForm

import datetime

from django.utils import timezone

class Bugs(models.Model):
    description = models.CharField(max_length=200)
    bug_type = models.CharField(max_length=20)
    report_date = models.DateTimeField("date reported")
    status = models.CharField(max_length=30)

# checking for test 
def report_date(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
