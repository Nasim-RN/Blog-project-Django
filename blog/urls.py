from django.urls import path
from . import views


urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.AllPostView.as_view(), name="posts-pages"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page")
]