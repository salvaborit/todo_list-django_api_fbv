from django.db import models


class Tag(models.Model):
    """ class for task tags table in db """
    name = models.CharField(max_length=5255)

    def __str__(self):
        return f'<Tag name: {self.name}>'

    class Meta:
        ordering = ['name']


class Task(models.Model):
    """ model for main tasks table in db """
    URGENCY_0 = '0'  # default
    URGENCY_1 = '1'
    URGENCY_2 = '2'

    URGENCY_CHOICES = [
        (URGENCY_0, 'Normal'),
        (URGENCY_1, 'Important'),
        (URGENCY_2, 'Very important'),
    ]

    title = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=True)
    urgency = models.CharField(
        max_length=1, choices=URGENCY_CHOICES, default=URGENCY_0)
    tags = models.ManyToManyField(Tag)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<Task title: {self.title}, created at: {self.created_at}>'

    class Meta:
        ordering = ['updated_at']
