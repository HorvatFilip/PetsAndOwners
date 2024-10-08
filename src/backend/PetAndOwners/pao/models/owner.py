from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
