from django.urls import path
from . import views


urlpatterns = [
    path('<slug:slug>/<slug:post_slug>/', views.Detail_View_of_Post.as_view(), name="post_detailed"),
    path('<slug:slug>/', views.List_of_Posts_View.as_view(), name="post_list"),
    path('', views.home),
]