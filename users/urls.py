
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from .views.users.sign_up import SignUp

urlpatterns = [
    path('sign-up', SignUp.as_view(), name='sign_up'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
