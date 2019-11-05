from django.urls import path
from . import views

urlpatterns = [
    path('', views.quetion_index, name='quetion_index'),
    path('create', views.quetion_create, name='quetion_create'),
    path('<int:question_ref>', views.question_detail, name='question_detail'),
    path('<slug:question_ref>', views.question_detail, name='question_detail')
]