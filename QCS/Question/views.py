from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import *
from django.forms import ModelForm
import re


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['topic', 'type', 'author', 'name', 'description', 'instruction', 'difficulty']



@require_http_methods(["GET"])
def quetion_index(request):
    # Get Latest Ten Questions
    if request.method == "GET":
        question_list = Question.objects.order_by('create_date')[:10]
        return render(request, 'question_index.html', {'question_list': question_list})


@require_http_methods(["GET", "POST"])
def quetion_create(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            # only professor can got to create question page
            if Course.objects.filter(professor=request.user).count() != 0:
                return render(request, 'question_create.html', {'form': QuestionForm()})
            else:
                return HttpResponse('You must be a professor of a course to create question', status=401)
        else:
            return HttpResponse('You are not logged in', status=401)
            
    elif request.method == "POST":
        # TODO Put Question into System
        if request.user.is_authenticated:
            # only professor can got to create question page
            if Course.objects.filter(professor=request.user).count() != 0:
                new_question = Question.objects.create(
                    type = QuestionType.objects.get(id = request.POST['type']),
                    author = User.objects.get(id = request.POST['author']),
                    last_editor = request.user,
                    name = request.POST['name'],
                    description = request.POST['description'],
                    instruction = request.POST['instruction'], 
                    difficulty = request.POST['difficulty']
                )
                for id in request.POST.getlist('topic'):
                    new_question.topic.add(QuestionTopic.objects.get(id = id))

                QuestionChangeLog.objects.create(
                    user = request.user,
                    question = new_question,
                    change_set = "Question Created",
                    previous_version = 0
                )

                return HttpResponse('Create Successfully')

            else:
                return HttpResponse('You must be a professor of a course to create question', status=401)

        else:
            return HttpResponse('You are not logged in', status=401)


@require_http_methods(["GET", "POST", "DELETE"])
def question_detail(request, question_ref):
    question = get_question(question_ref)

    if request.method == "GET":    
        info = {
            'name': question.name,
            'version': question.version,
            'author': question.author,
            'description': question.description,
            'instruction': question.instruction,
            'topic': [topic.name for topic in list(question.topic.all())],
            'forked_from' : question.forked_from
        }
        return render(request, 'question_detail.html', info)

    elif request.method == "POST":
        # TODO Update
        if request.user.is_authenticated:
            if request.user is question.author:

                return HttpResponse("Question " + question.Id + " Updated" )
            else:
                return HttpResponse('You are not the author of this question', status=401)
        else:
            return HttpResponse('You are not logged in', status=401)
            
    elif request.method == "DELETE":
        if request.user.is_authenticated:
            if request.user is question.author:
                id = question.Id
                question.delete()
                return HttpResponse("Question " + id + " Deleted" )
            else:
                return HttpResponse('You are not the author of this question', status=401)
        else:
            return HttpResponse('You are not logged in', status=401)


# Helper Function to Get Question Object via Question_Id or Question_Name
def get_question(question_ref):
    if isinstance(question_ref, int):
        question = get_object_or_404(Question, pk=question_ref)
    else:
        question_name_list = question_ref.split('-')
        roman_numeral = re.search('^(?=[MDCLXVI])M*(C[MD]|D?C*)(X[CL]|L?X*)(I[XV]|V?I*)$', question_name_list[-1], re.IGNORECASE)
        if roman_numeral:
            question_name_list.pop()
        question_name = " ".join([s.capitalize() for s in question_name_list])
        if roman_numeral:
            question_name += (" " + roman_numeral.string.upper())
        question = get_object_or_404(Question, name=question_name)
    return question


