from rest_framework import permissions


class IsSaleEmployeeOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        message = "Only sales employee assigned to the client can add or update"
        
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.sales_contact == request.user