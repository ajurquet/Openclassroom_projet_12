from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSaleEmployeeOrReadOnly, IsSupportEmployee

class ClientViewSet(viewsets.ModelViewSet):
    
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated , IsSaleEmployeeOrReadOnly | IsSupportEmployee]

    def get_queryset(self):
        return Client.objects.all()

    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         return [IsAdminUser()]
    #     return [IsSaleEmployeeOrReadOnly()]
