from django.contrib import admin
from .models import Owner, Pet

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'pet_type', 'get_owners')

    def get_owners(self, obj):
        return ", ".join([owner.name for owner in obj.owners.all()])

    get_owners.short_description = 'Owners'