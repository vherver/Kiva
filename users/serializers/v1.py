from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TokenObtainLifetimeSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        "no_active_account": "Not active email",
        "no_validated_account": "Not valid email",
    }
