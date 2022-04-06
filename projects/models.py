from django.db import models
from django.conf import settings

User_auth = settings.AUTH_USER_MODEL
# Create your models here.

# change model to collection
class Project(models.Model):
    name = models.CharField(max_length=200)  # change to title
    description = models.TextField()  # description
    members = models.ManyToManyField(User_auth, related_name="projects")

    def __str__(self):
        return self.name
