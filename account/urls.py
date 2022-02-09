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
    path("login/", views.LoginView.as_view(), name="login"),
    # Simple JWT
    # path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('rest-auth/', include('dj_rest_auth.urls')),
)
