from rest_framework import permissions


class IsAdminOnly(permissions.BasePermission):
    """Only admin can access this resource."""
    def has_permission(self, request, view):
        return (
            request.user.is_superuser or request.user.is_admin
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_superuser or request.user.is_admin
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allows access to the resource if a secure method is used or if
    the user is authenticated and is an admin or
    a superuser.
    """
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated and (
                    request.user.is_admin or request.user.is_superuser)))


class IsAuthorModeratorAdminOrReadOnly(permissions.BasePermission):
    """
    1.Allows access to the resource if a secure method is used, or in
    the case when the user is authenticated.
    2.Allows access to the object if a secure one is used
    the method or user is the author of the object -
    moderator, admin or superuser.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.is_admin_or_moderator
        )

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )
