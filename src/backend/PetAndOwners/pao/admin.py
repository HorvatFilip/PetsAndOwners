from django.contrib import admin
from .models import Owner, Pet

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'pet_type', 'owner')