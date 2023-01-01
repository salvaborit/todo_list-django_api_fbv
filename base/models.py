from django.db import models


class Tag(models.Model):
    """ class for task labels table in db """
    name = models.CharField(max_length=5255)

    def __str__(self):
        return f'<Tag name: {self.name}>'

    class Meta:
        ordering = ['name']


class Task(models.Model):
    """ model for main tasks table in db """
    title = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=True)
    tags = models.ManyToManyField(Tag, related_name='tasks')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<Task title: {self.title}, created at: {self.created_at}>'

    class Meta:
        ordering = ['updated_at']
