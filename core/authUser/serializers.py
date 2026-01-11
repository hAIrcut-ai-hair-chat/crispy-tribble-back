from rest_framework.serializers import ModelSerializer
from core.authUser.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = User
        read_only_fields = ["id", "passage_user_id", "created_at"]