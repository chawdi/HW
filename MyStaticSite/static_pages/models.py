from django.db import models

# Create your models here.
from django.db import models
from django.contrib.flatpages.models import FlatPage as BaseFlatPage

class StaticPage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    admin_only = models.BooleanField(default=False)

    def __str__(self):
        return self.title

