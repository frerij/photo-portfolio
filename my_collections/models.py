from django.db import models
from django.conf import settings

User_auth = settings.AUTH_USER_MODEL
# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover_image = models.URLField(max_length=500)

    def __str__(self):
        return self.title
