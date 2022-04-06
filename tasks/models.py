from django.db import models
from projects.models import Collection, User_auth

# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length=200)
    date_taken = models.DateTimeField()
    img_link = models.URLField(max_length=400)
    description = models.TextField()
    collection = models.ForeignKey(
        Collection, related_name="images", on_delete=models.CASCADE
    )
    photographer = models.ForeignKey(
        User_auth, null=True, related_name="images", on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.title
