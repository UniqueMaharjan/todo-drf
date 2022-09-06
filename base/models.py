from django.db import models
from user.models import User


class Todo(models.Model):
    creator = models.ForeignKey(User, on_delete= models.CASCADE, null= True, blank = True)
    title = models.CharField(max_length=150,null = True, blank = True)
    body = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
