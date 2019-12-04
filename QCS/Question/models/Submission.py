from django.db import models
from .Question import Question
from django.core.validators import MaxValueValidator, MinValueValidator


class Submission(models.Model):
    # Foreign Keys
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # Regular Fields
    name = models.CharField(max_length=256)
    student_code = models.CharField(max_length=256)
    correct = models.BooleanField(default=False)
    score = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    feedback = models.CharField(max_length=256)
    parameter = models.CharField(max_length=256)
    output = models.CharField(max_length=256)
    detail = models.CharField(max_length=256)
    status = models.CharField(max_length=256)

    def __str__(self):
        return self.name