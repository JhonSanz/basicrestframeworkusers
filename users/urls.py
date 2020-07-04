
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from .views.general import UserApi

urlpatterns = [
    path('user', UserApi.as_view(), name='sign_up'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
