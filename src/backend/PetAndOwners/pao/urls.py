from django.urls import path
from .views import (
    OwnersListApiView,
    OwnerApiView,
    PetsListApiView,
    PetApiView,
    OwnerPetsApiView,
    ShopApiView,
    stats_api
)


urlpatterns = [
    path("owners/", OwnersListApiView.as_view(), name="owners-list"),
    path("owner/<int:id>/", OwnerApiView.as_view(), name="owner-id"),
    path("owner/", OwnerApiView.as_view(), name="owner"),
    path("pets/", PetsListApiView.as_view(), name="pet-list"),
    path("pet/<int:id>/", PetApiView.as_view(), name="pet-id"),
    path("pet/", PetApiView.as_view(), name="pet"),
    path("owner/<int:id>/pets/", OwnerPetsApiView.as_view(), name="owner-pets"),
    path("shop/", ShopApiView.as_view(), name="shop"),
    path("stats/", stats_api.urls)
]
