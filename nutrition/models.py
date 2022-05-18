from django.db import models
from django.shortcuts import resolve_url


class Home(models.Model):
    LANGUAGE_ENG = 'eng'
    LANGUAGE_CZ = 'cz'

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENG, 'english'),
        (LANGUAGE_CZ, 'czech'),
    )

    @classmethod
    def as_view(cls):
        pass


class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    subject = models.TextField()
    phone_number = models.IntegerField()
    contact_at = models.DateField()

