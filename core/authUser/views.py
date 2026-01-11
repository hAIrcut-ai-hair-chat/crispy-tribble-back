from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from core.authUser.models import User
from core.authUser.serializers import UserSerializer
from core.authUser.permissions import AuthenticatedPermission
from rest_framework.decorators import api_view
from rest_framework.response import Response
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AuthenticatedPermission,)
    
    @action(detail=False, methods=["get"])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
    
    def get_queryset(self):
        return User.objects.filter(uuid=self.request.user.uuid)

@api_view(["GET", "POST"])
def ping(request):
    print("REQUISIÇÃO CHEGOU:", request.method)
    return Response({"status": "ok"})
