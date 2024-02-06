from rest_framework_simplejwt.views import TokenViewBase

from users.serializers.v1 import TokenObtainLifetimeSerializer


class TokenObtainPairView(TokenViewBase):
    serializer_class = TokenObtainLifetimeSerializer
