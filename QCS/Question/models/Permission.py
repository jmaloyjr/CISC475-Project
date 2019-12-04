from .UserRole import UserRole
from .Course import Course
from django.db import models
from django.contrib.auth.models import User


class Permission(models.Model):
    class Meta:
        unique_together = ('user', 'role', 'course')


    # Foreign Keys    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ": " + str(self.role) + " - " + str(self.course)