from django.db import models

# Create your models here.

class Bugs(models.Model):
    description = models.CharField(max_length=200)
    bug_type = models.CharField(max_length=20)
    report_date = models.DateTimeField("date reported")
    status = models.CharField(max_length=30)
