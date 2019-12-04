from .HelperFunction import is_professor, is_current_TA
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def quetion_create(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, 'question-create.html')
        else:
            return HttpResponse('You are not logged in', status=401)
            
    # elif request.method == "POST":
    #     # TODO Put Question into System
    #     if request.user.is_authenticated:
    #         question_form = QuestionForm(request.POST)
    #         if question_form.is_valid():
    #             q = question_form.save(commit=False)
    #             #q.last_editor = request.user
    #             q.user_save(request.user)
    #             question_form.save_m2m()

    #             return HttpResponse('Create Successfully')
    #         else:
    #             return render(request, 'question-create.html', {'form': question_form})
    #     else:
    #         return HttpResponse('You are not logged in', status=401)
