from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('add/', views.add_rec),
    path('show/',views.get_all_rec),
    path('register/',views.register),
    path('register/add/',views.regadd),
    path('userlist/<str:curpage>/', views.userlist)

]