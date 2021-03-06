from django.urls import (
    path,
    include,
)
from account import views
from rest_framework_simplejwt import views as jwt_views

app_name = "account"

urlpatterns = (
    path("", views.UserList.as_view(), name="list"),
    path("<int:pk>", views.UserDetail.as_view(), name="detail"),
    # path("register/", views.RegisterView.as_view(), name="register"),
    path("auth/", views.AuthView.as_view(), name="auth"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    # Simple JWT
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
)
