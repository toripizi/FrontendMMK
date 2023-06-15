from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('create_log_message', views.create_log_message),
        path('log_messages', views.log_messages),
]
