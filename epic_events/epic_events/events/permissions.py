from django.utils import timezone
from rest_framework import permissions


class IsSupportEmployeeOrReadOnly(permissions.BasePermission):
    message = "Support employee can only read data"

    def has_permission(self, request, view):

        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.support_contact == request.user


class IsEventFinish(permissions.BasePermission):
    message = "An event can't be updated once it's finished"

    def has_permission(self, request, view):

        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.event_date > timezone.now()


class IsSaleEmployeeConnectedToTheEventOrReadOnly(permissions.BasePermission):
    message = "Can't update an event if the employee is not assigned to it"

    def has_permission(self, request, view):

        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.contract.client.sales_contact == request.user
