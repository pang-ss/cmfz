from django.urls import path

from pss_show import views

app_name = "pss_show"
urlpatterns = [
    path('index/', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('getcode/', views.get_code, name="getcode"),
    path('loginlogic/', views.loginlogic, name="loginlogic"),
]