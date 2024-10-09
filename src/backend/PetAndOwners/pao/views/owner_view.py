from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Owner
from ..serializers import OwnerSerializer, PetSerializer


class OwnersListApiView(APIView):
    def get(self, request):
        owners = Owner.objects.all()
        serializer = OwnerSerializer(owners, many=True)
        return Response(serializer.data)

class OwnerApiView(APIView):
    def get(self, request, id=None):
        if id is not None:
            try:
                owner = Owner.objects.get(id=id)
                serializer = OwnerSerializer(owner)
                return Response(serializer.data)
            except Owner.DoesNotExist:
                return Response({"error":f"Owner with id: {id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error":"Owner id not provided"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id=None):
        if id is None:    
            serializer = OwnerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error":"Post request should not include id"}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None):
        if id is not None:
            try:
                owner = Owner.objects.get(id=id)
                serializer = OwnerSerializer(owner, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Owner.DoesNotExist:
                return Response({"error":f"Owner with id: {id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error":"Owner id not provided"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        if id is not None:
            try:
                owner = Owner.objects.get(id=id)
                owner.delete()
                return Response({"message":f"Owner with id: {id} successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
            except Owner.DoesNotExist:
                return Response({"error":f"Owner with id: {id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error":"Owner id not provided"}, status=status.HTTP_400_BAD_REQUEST)


class OwnerPetsApiView(APIView):
    def get(self, request, id=None):
        if id is not None:
            try:
                owners_pets = Owner.objects.get(id=id).pets
                serializer = PetSerializer(owners_pets, many=True)
                return Response(serializer.data)
            except Owner.DoesNotExist:
                return Response({"error":f"Owner with id: {id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error":"Owner id not provided"}, status=status.HTTP_400_BAD_REQUEST)


