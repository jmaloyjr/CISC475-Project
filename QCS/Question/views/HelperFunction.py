from django.shortcuts import get_object_or_404
from ..models.Question import Question
from ..models.Permission import Permission
from ..models.UserRole import UserRole
from datetime import datetime
import re


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

# Check if user is TA for current semester
def is_current_TA(user):
    def check_course_is_current(course): 
        now = datetime.now()
        year = now.year
        month = now.month

        semester = None

        if month in [1]:
            semester = "WI"
        elif month in [2, 3, 4, 5]:
            semester = "SP"
        elif month in [6, 7, 8]:
            semester = "SU"
        else:
            semester = "FA"

        return course.semester == semester and course.year == year

    permissions = Permission.objects.filter(user = user).filter(role = UserRole("TA"))
    if permissions.count() != 0:
        courses = [p.course for p in permissions]
        if len(list(filter(check_course_is_current, courses))) != 0:
            return True

    return False

# Check if user is/was professor
def is_professor(user):
    Permission.objects.filter(user = user).filter(role = UserRole("Professor")).count() != 0

# Check If Current User Have Permission Over Question
def check_permission(user, question, request_method):
    if request_method == "GET":
        # User is admin or superuser
        if user.is_staff or user.is_superuser:
            return True

        # User is/was a professor of a course
        if is_professor(user):
            return True

        # User is current TA of a course
        if is_current_TA(user):
            return True

        return False

    elif request_method == "PUT":
        # User is admin or superuser
        if user.is_staff or user.is_superuser:
            return True

        # User is/was a professor of a course
        if is_professor(user):
            return True

        # User is current TA of a course
        if is_current_TA(user):
            return True

        return False

    elif request_method == "POST":
        # User is admin or superuser
        if user.is_staff or user.is_superuser:
            return True

        # User is/was a professor of a course
        if is_professor(user):
            return True

        # User is current TA of a course
        if is_current_TA(user):
            return True

        return False

    elif request_method == "DELETE":
        # User is admin or superuser
        if user.is_staff or user.is_superuser:
            return True

        # User is/was a professor of a course
        if is_professor(user):
            return True

        return False

    return False