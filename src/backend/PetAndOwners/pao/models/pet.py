from django.db import models
from .owner import Owner

class Pet(models.Model):
    name = models.CharField(max_length=50)
    
    class PetType(models.TextChoices):
        UNDEFINED = "undefined", "Undefined"
        CAT = "cat", "Cat"
        DOG = "dog" "Dog"
    pet_type = models.CharField(
        max_length=9,
        choices=PetType.choices,
        default=PetType.UNDEFINED
    )

    owner = models.ForeignKey(to=Owner, null=True, on_delete=models.SET_NULL, related_name="pets")




    def __str__(self):
        return self.name
