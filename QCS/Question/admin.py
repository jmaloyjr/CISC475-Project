from django.contrib import admin
from .models import *


# Register your models here.
root_admin = [Question, Tag, Course]
admin.site.register(root_admin)
