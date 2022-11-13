from django.contrib.auth.models import AbstractUser
from django.db import models

# Create Models Here
class User(AbstractUser):
    pass

class Park(models.Model):

    name = models.CharField("Full name", max_length=100)
    address = models.CharField("Address", max_length=100)
    city = models.CharField("City", max_length=100)
    state = models.CharField("State", max_length=100)
    zipcode = models.CharField("ZIP code", max_length=12)

    basketball = models.BooleanField()
    football = models.BooleanField()
    baseball = models.BooleanField()
    volleyball = models.BooleanField()
    tennis = models.BooleanField()
    handball = models.BooleanField()
    cricket = models.BooleanField()

    def __str__(self):
        return self.name




    class Meta:
        verbose_name = "Park"
        verbose_name_plural = "Parks"
