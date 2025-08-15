from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer



class UserRegisterView(APIView):
    def post(self, request):
        serializers = UserRegisterSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTR_201_CREATED)
        return Response(status.HTTR_400_BAD_REQUEST)

