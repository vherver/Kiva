from django.urls import path

from users.views.v1 import TokenObtainPairView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="v1_login"),
]
