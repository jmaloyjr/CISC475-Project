from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('CreateQuestion/', views.create, name='create_question')
]