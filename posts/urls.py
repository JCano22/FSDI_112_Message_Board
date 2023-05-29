from django.urls import path
from posts import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("new/", views.PostCreateView.as_view(), name="new"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
]
