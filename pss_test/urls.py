from django.urls import path
from pss_test import views

app_name = "pss_test"

urlpatterns = [
    path("main/", views.main, name="main"),
    path("detail/", views.detail, name="detail"),
    path("regist/", views.regist, name="regist"),
    path("modify/", views.modify, name="modify"),
]