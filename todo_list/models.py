from django.db import models


class Tasks(models.Model):
    """ model for main tasks table in db """
    name = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Labels(models.Model):
    """ class for task labels table in db """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
