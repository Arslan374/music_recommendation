# recommend/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new_user, name='new_user'),
    path('existing/', views.existing_users, name='existing_users'),
    path('existing/<int:user_id>/', views.existing_user_recommendations, name='existing_user_recommendations'),
]
