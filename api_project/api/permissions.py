from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admins to edit, but authenticated users can view.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  # Read-only access is allowed for any user
        return request.user and request.user.is_staff  # Only admin can modify
