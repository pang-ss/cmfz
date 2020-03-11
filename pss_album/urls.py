from django.urls import path

from pss_album import views
app_name = "pss_album"

urlpatterns = [
    path('getAllAlbum/', views.getAllAlbum, name="getAllAlbum"),
    path('add_album/', views.add_album, name="add_album"),
    path('getChapter/', views.getChapter, name="getChapter"),
    path('add_chapter/', views.add_chapter, name="add_chapter"),
    path('edit_album/', views.edit_album, name="edit_album"),
    path('change_album/', views.change_album, name="change_album"),
    path('edit_chapter/', views.edit_chapter, name="edit_chapter"),
    path('change_chapter/', views.change_chapter, name="change_chapter"),

]