from rest_framework import viewsets

from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsEventFinish, IsSupportEmployeeOrReadOnly,  \
                                        IsSaleEmployeeConnectedToTheEventOrReadOnly


class EventViewSet(viewsets.ModelViewSet):

    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsSupportEmployeeOrReadOnly,
                          IsSaleEmployeeConnectedToTheEventOrReadOnly, IsEventFinish]

    def get_queryset(self):
        return Event.objects.all()
