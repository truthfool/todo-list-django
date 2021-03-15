from django.db import models
from django.utils import timezone
# Create your models here.
class ToDoListModel(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=1000,blank=True)
    date=models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.title