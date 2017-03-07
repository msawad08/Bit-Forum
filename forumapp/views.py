from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Question, Answer, Comment;


# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'index.html', context)
