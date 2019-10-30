from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def create(request):
    return render(request, 'create_question.html')

def viewQuestion(request):
    return render(request, 'view_question.html')