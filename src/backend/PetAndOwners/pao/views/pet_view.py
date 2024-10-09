from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Pet
from ..serializers import PetSerializer


class PetsListApiView(APIView):
    def get(self, request):
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)

class PetApiView(APIView):
    def get(self, request, id=None):
        if id is not None:
            try:
                pet = Pet.objects.get(id=id)
                serializer = PetSerializer(pet)
                return Response(serializer.data)
            except Pet.DoesNotExist:
                return Response({"error":f"Pet with id: {id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error":"Pet id not provided"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id=None):
        if id is None:    
            serializer = PetSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error":"Post request should not include id"}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None):
        if id is not None:
            try:
                pet = Pet.objects.get(id=id)
                serializer = PetSerializer(pet, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Pet.DoesNotExist:
                return Response({"error":f"Pet with id: {id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error":"Pet id not provided"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        if id is not None:
            try:
                pet = Pet.objects.get(id=id)
                pet.delete()
                return Response({"message":f"Pet with id: {id} successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
            except Pet.DoesNotExist:
                return Response({"error":f"Pet with id: {id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error":"Pet id not provided"}, status=status.HTTP_400_BAD_REQUEST)



