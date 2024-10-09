from django.urls import path
from .views import OwnersListApiView, OwnerApiView


urlpatterns = [
    path("users/", OwnersListApiView.as_view(), name="users-list"),
    path("user/<int:id>/", OwnerApiView.as_view(), name="users-list"),
    path("user/", OwnerApiView.as_view(), name="users-list")
]
