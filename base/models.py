from django.db import models


class Task(models.Model):
    """ model for main tasks table in db """
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<Task title: {self.title}, created at: {self.created_at}>'


class Label(models.Model):
    """ class for task labels table in db """
    name = models.CharField(max_length=50)
    # task = models.ForeignKey(Task, on_delete=TOBEDEFINED!!)

    def __str__(self):
        return f'<Label name: {self.name}>'
