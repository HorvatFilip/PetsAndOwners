from ninja import NinjaAPI
from django.db.models import Count
from pao.models import Pet, Owner

api = NinjaAPI()


@api.get("stats/same-pets")
def stats_same_pets(request):
    pet_stats = {}
    for pet in Pet.objects.all():
        numof_same_owners = 0
        if pet in 
