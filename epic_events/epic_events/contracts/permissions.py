from rest_framework import permissions


class IsSaleEmployeeConnectedToTheContractOrReadOnly(permissions.BasePermission):

      def has_object_permission(self, request, view, obj):

        message = ""
        
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.client.sales_contact == request.user
      
