from rest_framework import viewsets
from .models import Contract
from .serializers import ContractSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSaleEmployeeConnectedToTheContractOrReadOnly, \
    IsSupportEmployeeOrReadOnly


class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated,
                          IsSaleEmployeeConnectedToTheContractOrReadOnly,
                          IsSupportEmployeeOrReadOnly]

    def get_queryset(self):
        return Contract.objects.all()
