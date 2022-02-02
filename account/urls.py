from django.urls import path
from account import views

app_name = "account"

urlpatterns = (
    path("", views.UserList.as_view(), name="list"),
    path("<int:pk>", views.UserDetail.as_view(), name="detail"),
    path("revoke-token/", views.RevokeToken.as_view(), name="revoke"),
)
