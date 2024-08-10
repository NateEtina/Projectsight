
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Task, Project, User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['executors']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['checking']