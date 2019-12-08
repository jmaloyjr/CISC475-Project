from django.urls import path
from .views.QuestionIndex import quetion_index
from .views.QuestionCreate import quetion_create
from .views.QuestionDetails import question_detail


urlpatterns = [
    path('', quetion_index, name='quetion_index'),
    path('create', quetion_create, name='quetion_create'),
    path('<int:question_ref>', question_detail, name='question_detail'),
    path('<slug:question_ref>', question_detail, name='question_detail')
]