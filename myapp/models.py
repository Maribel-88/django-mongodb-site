# myapp/models.py
from django.db import models

class UserProfile(models.Model):
    # Django + Djongo maps this automatically to MongoDB's unique _id field
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

