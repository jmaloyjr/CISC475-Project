from django.db import models
from django.contrib.auth.models import User


class QuestionChangelog(models.Model):
    # Foreign Keys
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    question = models.ForeignKey('Question',  null=True, blank=True, on_delete=models.SET_NULL)
    
    # Regular Fields
    change_set = models.CharField(max_length=256)
    previous_version = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.question) + ": Version " + str(self.previous_version)