from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100,verbose_name='project name')
    description = models.TextField()
    executors = models.ManyToManyField(User, related_name='participants', blank=True)
    deadline = models.DateField(auto_now=False,help_text='YYYY-MM-DD')
    
    created = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name

class Task(models.Model):
    body = models.TextField()
    executiontime = models.IntegerField(help_text = 'Hour(s)',verbose_name='execution time')
    checking = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)
    
    created = models.DateField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.body
    
