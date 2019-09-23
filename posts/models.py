""" Posts models. """

# Django
from django.db import models


# Define table

class User(models.Model):
    """ User model. """

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)

    # esta almacena la hora tambien
    created = models.DateTimeField(auto_now_add=True)
    modifique = models.DateTimeField(auto_now=True)