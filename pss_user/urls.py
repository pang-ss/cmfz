from django.urls import path

from pss_user import views

app_name = "pss_user"
urlpatterns = [
    path('get_user/', views.get_user, name="get_user"),
    path('change_user/', views.change_user, name="change_user"),
    path('get_data/', views.get_data, name="get_data"),
    path('get_map/', views.get_map, name="get_map"),

]