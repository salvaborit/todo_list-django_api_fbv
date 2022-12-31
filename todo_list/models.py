from django.db import models


class Tasks(models.Model):
    """ model for main tasks table in db """
    name = models.CharField(max_length=500)
    # label = models.ForeignKey(Labels, )


class Labels(models.Model):
    """ class for task labels table in db """
    name = models.CharField(max_length=50)
