from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('setup', views.setup),
    path('monitoring', views.monitoring),
    path('profile', views.profile),
    path('get_rabbits_data/', views.get_rabbits_data, name='get_rabbits_data'),
    path('post_test_data/', views.post_test_data, name='post_test_data')
]