from rest_framework.permissions import BasePermission
from utils.passage import authenticate_passage

class AuthenticatedPermission(BasePermission):
    def has_permission(self, request, view):
        user = authenticate_passage(request)
        if user:
            request.user = user
            return True
        return False
    