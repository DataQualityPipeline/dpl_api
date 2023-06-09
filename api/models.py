from django.db import models

class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.email + ", " + self.role
    
    