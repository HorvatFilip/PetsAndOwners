from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Pet, Owner


class ShopApiView(APIView):
    def post(self, request):
        required_keys = ["owner_id","pet_id","action"]
        missing_keys = [key for key in required_keys if key not in request.data]
        missing_values = [key for key in required_keys if key in request.data and not request.data[key]]
        if len(missing_keys) == 0 and len(missing_values) == 0:
            owner_id = request.data["owner_id"]
            pet_id = request.data["pet_id"]
            action = request.data["action"]
            try:
                owner = Owner.objects.get(id=owner_id)
                pet = Pet.objects.get(id=pet_id)
                if action == "buy":
                    if pet.owner == owner:
                        return Response({"message":f"Owner '{owner.name}' already owns '{pet.name}'"})
                    pet.owner = owner
                    pet.save()
                    return Response({"message":f"Owner '{owner.name}' successfully bought '{pet.name}'"})
                elif action == "sell":
                    if pet.owner != owner:
                        return Response({"message":f"Owner '{owner.name}' can't sell '{pet.name}'"})
                    pet.owner = None
                    pet.save()
                    return Response({"message":f"Owner '{owner.name}' successfully sold '{pet.name}'"})
                else:
                    return Response({"error":f"Invalid action: {action}"}, status=status.HTTP_400_BAD_REQUEST)    
            except Owner.DoesNotExist:
                return Response({"error":f"Owner with id: {owner_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
            except Pet.DoesNotExist:
                return Response({"error":f"Pet with id: {pet_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        error_str = ""
        if len(missing_keys) > 0:
            error_str = "missing keys: " + ",".join(missing_keys) + " "
        if len(missing_values) > 0:
            error_str = error_str + "missing values: " + ",".join(missing_values)
        return Response({"error": error_str})
