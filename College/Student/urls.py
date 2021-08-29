from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('Studnet_From', views.Studnet_From),
    path('Display_info', views.Display_info),
    path("Display_accdemic/<int:pk>", views.Display_accdemic, name="Display_accdemic"),
    path('Update_And_Delete.html', views.Update_And_Delete),
    path('Search.html', views.Search),
    path("Confirm_delet/<int:pk>", views.Confirm_delet, name="Confirm_delete_list"),
    path("Update_userlst/<int:pk>", views.Update_user, name="Update_user_list"),
    path("Update_userlst/Submit_Form", views.Update_From_userlst, name="Update_user_list"),
    path("Search", views.Search, name="Search"),

]
