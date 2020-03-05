from django.urls import path

from pss_banner import views
app_name = "pss_banner"

urlpatterns = [
    path('add_banner/', views.add_banner, name="add_banner"),
    path('get_banner/', views.get_banner, name="get_banner"),
    path('change_banner/', views.change_banner, name="change_banner"),
]