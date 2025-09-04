# models.py
# models.py
from django.db import models

class Post(models.Model):
    Name = models.CharField(max_length=200)
   
    def __str__(self):
        return self.Name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.email}"


