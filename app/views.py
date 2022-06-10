from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, generics
from .models import UserDetails
from .serializers import RegistrationSerializer
from rest_framework import status


# Create your views here.


class RegistrationAPIView(viewsets.ModelViewSet):
    http_method_names = ('post', 'get')
    serializer_class = RegistrationSerializer
    queryset = UserDetails.objects.all()

    # pagination_class = LargeResultsSetPagination
    # def get_queryset(self):
    #     return UserDetails.objects.all().filter(is_verified=True)
    def get_queryset(self):
        queryset = UserDetails.objects.all()
        active = self.request.query_params.get('is_active', '')
        if active:
            if active == "False":
                active = False
            elif active == "True":
                active = True
            else:
                return queryset
            return queryset.filter(is_active=active)
        return queryset

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

            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

