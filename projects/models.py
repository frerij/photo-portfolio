from django.db import models
from django.conf import settings

User_auth = settings.AUTH_USER_MODEL
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    members = models.ManyToManyField(User_auth, related_name="projects")

    def __str__(self):
        return self.name
