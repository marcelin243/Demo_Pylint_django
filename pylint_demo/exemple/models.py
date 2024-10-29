from django.db import models

# Create your models here.
# myapp/models.py


class User(models.Model):
    username = models.CharField(max_length=150,null=False)
    email = models.EmailField(null=False)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.username
