from ninja import NinjaAPI
from django.db.models import Count
from pao.models import Pet, Owner

stats_api = NinjaAPI()

@stats_api.get("/shared-owners-count")
def stats_same_pets(request):
    pets_with_multiple_owners = Pet.objects.annotate(numof_owners=Count('owners')).filter(numof_owners__gt=1)
    unique_owner_ids = set()
    for pet in pets_with_multiple_owners:
        owners = pet.owners.values_list('id', flat=True)
        unique_owner_ids.update(owners)

    return {"shared-owners-count": len(unique_owner_ids)}
    
