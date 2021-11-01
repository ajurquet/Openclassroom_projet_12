from rest_framework import permissions


class IsSupportEmployeeOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):

        message = ""
        
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.support_contact == request.user


class IsSaleEmployeeOrReadOnly(permissions.BasePermission):

      def has_object_permission(self, request, view, obj):

        message = ""
        
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.sales_contact == request.user
