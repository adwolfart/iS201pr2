from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    paragraph = models.TextField(null=False)
    date = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        return str(self.id) + " " + self.title
