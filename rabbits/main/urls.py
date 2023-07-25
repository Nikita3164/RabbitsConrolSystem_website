from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('setup', views.setup),
    path('monitoring', views.monitoring),
    path('profile', views.profile)
]