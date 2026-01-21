from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from access_control.models import Permission

class CustomPermissionMixin:
    def check_resource_permission(self, request, action):
        user = request.user
        resource_name = self.__class__.__name__.lower().replace('viewset', '')
        
        permission_exists = Permission.objects.filter(
            user=user, 
            resource__name=resource_name, 
            action=action.upper()
        ).exists()
        
        if not permission_exists:
            self.permission_denied(
                request, 
                message='You do not have permission to perform this action.'
            )

class DocumentViewSet(CustomPermissionMixin, viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        self.check_resource_permission(request, 'read')
        return Response(["Document 1", "Document 2"])

    def create(self, request):
        self.check_resource_permission(request, 'write')
        return Response({"status": "Document created"})
