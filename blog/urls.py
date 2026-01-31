from django.urls import path
from .views import cat_list, cat_detail

urlpatterns = [
    path("cat/<int:pk>/", cat_detail, name="cat_detail"),
    path("", cat_list, name="home"),
]
