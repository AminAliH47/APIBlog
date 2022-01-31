from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = (
    path("", views.ArticlesList.as_view(), name="list"),
    path("<int:pk>", views.ArticlesDetail.as_view(), name="detail"),
)
