from django.urls import path

from pss_article import views
app_name = "pss_article"

urlpatterns = [
    path('upload_img/', views.upload_img, name="upload_img"),
    path('get_all_img/', views.get_all_img, name="get_all_img"),
    path('add_article/', views.add_article, name="add_article"),
    path('getALLArticle/', views.getALLArticle, name="getALLArticle"),
    path('change_article/', views.change_article, name="change_article"),
    path('edit_article/', views.edit_article, name="edit_article"),

]