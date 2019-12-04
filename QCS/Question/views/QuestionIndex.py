from django.shortcuts import render
from django.contrib.auth.models import User
from ..models.Question import Question
from ..models.QuestionTopic import QuestionTopic
from ..models.Course import Course
from django.views.decorators.http import require_http_methods



@require_http_methods(["GET"])
def quetion_index(request):
    # Get Latest Ten Questions
    if request.method == "GET":
        question_list = Question.objects.order_by('create_date')[:10]
        info = {
            'question_list': question_list,
            'question_titles': Question.objects.all(),
            'courses': Course.objects.all(),
            'authors': User.objects.all(),
            'topics': QuestionTopic.objects.all()
        }
        return render(request, 'question-index.html', info)
