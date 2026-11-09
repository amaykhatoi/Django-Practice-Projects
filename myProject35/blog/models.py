from django.db import models

# Create your models here.
class UserList(models.Model):
    name = models.CharField(max_length=100)
    subscriber = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    