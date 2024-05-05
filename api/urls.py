from django.urls import path
from . import views
app_name = 'api'

urlpatterns = [
    path('users', views.users, name='users'),
    path('health', views.health_check, name='health'),
]