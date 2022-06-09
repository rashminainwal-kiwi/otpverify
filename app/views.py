from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.viewsets import GenericViewSet
from .models import User
from .serializers import RegistrationSerializer
from rest_framework import status


# Create your views here.

class RegistrationAPIView(viewsets.ModelViewSet):
    http_method_names = ('post', 'get')
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "Message": "User created successfully",

                "User": serializer.data}, status=status.HTTP_201_CREATED
            )
        else:
            # return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
