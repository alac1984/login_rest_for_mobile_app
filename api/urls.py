from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.UserCreateAPIView.as_view(), name='create')
]
