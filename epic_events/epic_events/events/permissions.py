from django.utils import timezone
from rest_framework import permissions


class IsSupportEmployeeOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):

        message = ""
        
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.support_contact == request.user


class IsEventFinish(permissions.BasePermission):

    def has_permission(self, request, view):

        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):

        message = ""
        
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.event_date > timezone.now()


class IsSaleEmployeeConnectedToTheEventOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        message = ""
        
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.contract.client.sales_contact == request.user
      
