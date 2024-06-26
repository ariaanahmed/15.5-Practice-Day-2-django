from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return f'Musician: {self.first_name} {self.last_name}'
