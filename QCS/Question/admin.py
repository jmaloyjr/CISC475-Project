from django.contrib import admin
from .models.Course import Course
from .models.QuestionTopic import QuestionTopic
from .models.QuestionType import QuestionType
from .models.Question import Question
from .models.Submission import Submission
from .models.QuestionChangelog import QuestionChangelog
from .models.UserRole import UserRole
from .models.Permission import Permission


# Register your models here.
root_admin = [
    Course, 
    QuestionTopic, 
    QuestionType, 
    Question, 
    Submission, 
    QuestionChangelog, 
    UserRole, 
    Permission
]

admin.site.register(root_admin)
