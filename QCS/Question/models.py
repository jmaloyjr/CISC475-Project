from django.db import models
# import datetime


class Tag(models.Model):
    tag_text = models.CharField(max_length=200)

    def __str__(self):
        return self.tag_text


class Course(models.Model):
    course_text = models.CharField(max_length=200)

    def __str__(self):
        return self.course_text


class Question(models.Model):
    question_name = models.CharField(max_length=200)
    question_text = models.CharField(max_length=200)
    create_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    version = models.IntegerField(default=1)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_name
