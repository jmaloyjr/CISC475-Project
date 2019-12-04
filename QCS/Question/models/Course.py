from django.db import models
from .Question import Question
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class Course(models.Model):
    class Meta:
        unique_together = ('year', 'semester', 'code', 'section')


    # Regular Fields
    name = models.CharField(max_length=256)
    code = models.PositiveSmallIntegerField(default=100, validators=[MinValueValidator(100), MaxValueValidator(999)])
    section = models.PositiveSmallIntegerField(default=100, validators=[MinValueValidator(0), MaxValueValidator(999)])
    year = models.PositiveSmallIntegerField(default=datetime.now().year, validators=[MinValueValidator(1000), MaxValueValidator(9999)])

    # Semester Choice - ENUM
    FALL = 'FA'
    WINTER = 'WI'
    SPRING = 'SP'
    SUMMER = 'SU'
    SEMESTER = [
        (FALL, 'Fall'),
        (WINTER, 'Winter'),
        (SPRING, 'Spring'),
        (SUMMER, 'Summer')
    ]
    semester = models.CharField(
        max_length=2,
        choices=SEMESTER,
        default=FALL
    )

    # Foreign Keys
    question = models.ManyToManyField(Question, blank=True)
    
    def __str__(self):
        return " ".join([str(self.year), self.get_semester_display(), "CISC" + str(self.code) + "-" + str(self.section), self.name])