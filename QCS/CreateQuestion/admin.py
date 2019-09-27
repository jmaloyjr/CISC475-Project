from django.contrib import admin
from .models import *


# Register your models here.
myModels = [Question, Tag, Course]
admin.site.register(myModels)
