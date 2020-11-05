from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30, null=True)
    lname = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    gender = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.fname}"
    



