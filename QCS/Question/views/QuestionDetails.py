from .HelperFunction import get_question
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods


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
            'difficulty': question.difficulty,
            'topic': question.topic.all()
        }
        return render(request, 'question-detail.html', info)

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


