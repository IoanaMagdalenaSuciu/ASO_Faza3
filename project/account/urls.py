from django.urls import path
from .views import register
from django.contrib.auth import views
from . import views as local_views
urlpatterns = [
    path('singup/',register,name='singup'),
    path('login/', local_views.login_view, name='login'),
    path('logout/', local_views.logout_view, name='logout'),
]