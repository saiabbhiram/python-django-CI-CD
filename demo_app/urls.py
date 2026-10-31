from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('health/', views.health_check_view, name='health_check'),
]
