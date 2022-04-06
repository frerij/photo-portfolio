from django.db import models
from projects.models import Project, User_auth

# Create your models here.


#change model name to image
class Task(models.Model):
    name = models.CharField(max_length=200) #change to title
    start_date = models.DateTimeField() #change to date taken
    due_date = models.DateTimeField() #add url/img link 
    is_completed = models.BooleanField(default=False, null=False) #change to description
    project = models.ForeignKey(
        Project, related_name="tasks", on_delete=models.CASCADE #change to collections
    )
    assignee = models.ForeignKey(
        User_auth, null=True, related_name="tasks", on_delete=models.SET_NULL #photographer
    )

    def __str__(self):
        return self.name
