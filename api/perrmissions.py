from rest_framework import permissions
from rest_framework.response import Response

class IsOwnerPermission(permissions.DjangoModelPermissions):
    
    def has_object_permission(self, request, view,obj):
        if not request.user == obj.creator:
            return False
        return super().has_permission(request, view)