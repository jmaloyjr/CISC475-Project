from django.db import models


class UserRole(models.Model):
    # Regular Fields
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name
        