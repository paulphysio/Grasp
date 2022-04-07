from django.urls import path
from . import views


urlpatterns = [
    path('home', views.Home, name="home"),
    path('', views.create, name="create"),
    path('list/', views.list, name = "list"),
    path('boot/', views.boot, name = "boot"),
    path('notify/', views.notify, name = "notify")

]