from rest_framework import permissions


class IsSaleEmployeeOrReadOnly(permissions.BasePermission):
    message = "Only sales employee assigned to the client can add or update"

    def has_permission(self, request, view):

        return request.user
    
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.sales_contact == request.user 


class IsSupportEmployee(permissions.BasePermission):

    def has_permission(self, request):

        return request.user
        # if request.user.role == 'SUPPORT':
        #     if request.method == 'GET':
        #         return True
        #     elif request.method == 'POST':
        #         return False
        #     return False

    
    def has_object_permission(self, request, view, obj):
                
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.role == 'SUPPORT':
            return False

