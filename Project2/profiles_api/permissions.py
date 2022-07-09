from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ Allow user to edit their own profile """

    def has_object_permission(self, request, view, obj):
        """ Check user is trying to edit their own profile """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id #if obj.id == request.user.id return true else return false


class UpdateOwnStatus(permissions.BasePermission):
    """ Allow users to update their own status """

    def has_object_permission(self, request, view, obj):
        """ Chechk the user is trying to update their own status """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id