from rest_framework import permissions


class IsSaleEmployeeOrReadOnly(permissions.BasePermission):
    message = "Only sales employee assigned to the client can add or update"

    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.role == 'SUPPORT':
            return False
        return True

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.sales_contact == request.user
