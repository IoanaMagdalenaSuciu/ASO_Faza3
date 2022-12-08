from chat import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home', ),
    path('account/', include('account.urls')),
    path('<str:chat>/', views.chat, name='privateChat'),
    path('messages/<str:chat>/', views.getMessages, name='messages'),
    path('send', views.send, name='send'),
    path('view', views.private_chat, name='view'),
    path('invite', views.invite, name='invite')

]