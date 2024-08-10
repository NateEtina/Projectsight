from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Task, Project, User
from .forms import ProjectForm, TaskForm,UserForm


def loginUser(request):
    page = 'login'
    phrase = 'the user exist'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            phrase = f'user {username} does\'nt exist'
              
    context = {
        'phrase':phrase,
        'page':page,
    }
    return render(request, 'managertool/login_signup.html', context)

def signupUser(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

    context = {
        'form': form,
        }
    return render(request, 'managertool/login_signup.html', context)

def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'managertool/logoutconf.html')

@login_required(login_url='login')
def index(request) :
    user = request.user
    projects = Project.objects.filter(author__username=str(user.username))
    n_project = projects.count()
    n_task = 0
    projects_details = []
    for p in projects:
        projects_details.append((p, Task.objects.filter(project__name=str(p.name)).count()))
        n_task += Task.objects.filter(project__name=str(p.name)).count()

    context = {
        'user':user,
        'projects':projects,
        'n_project': n_project,
        'projects_details':projects_details,
        'n_task': n_task,
    }
    return render(request, 'managertool/index.html', context)

@login_required(login_url='login')
def projectFrame(request, pk):
    project = Project.objects.get(id=pk)
    tasks = Task.objects.filter(project__name=str(project.name))
    achievedTask = []
    unachievedTask = []

    for item in tasks:
        if item.checking == True :
            achievedTask.append(item)
        elif item.checking == False:
            unachievedTask.append(item)

    context = {
        'project':project,       
        'achievedTasks' : achievedTask,
        'unachievedTasks':unachievedTask,
        'task_count':tasks.count(),
    }
    return render(request, 'managertool/projectframe.html', context)

@login_required(login_url='login')
def addProject(request):
    form = ProjectForm(initial={'author':request.user})
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'managertool/addproject.html', context)

@login_required(login_url='login')
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST' :
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()

        return redirect('project-frame', pk=project.id)
    context = {'form':form}
    return render(request, 'managertool/addproject.html', context)

@login_required(login_url='login')
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST' :
        project.delete()
        return redirect('home')
    return render(request, 'managertool/dropproject.html', {'project':project})

@login_required(login_url='login')
def addTask(request, pk):
    project = Project.objects.get(id=pk)
    form = TaskForm(initial={'project':project})
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('project-frame', pk=project.id)

    context = {'form':form}
    return render(request, 'managertool/addtask.html', context)

@login_required(login_url='login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    project = task.project
    form = TaskForm(instance=task)
    if request.method == 'POST' :
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('project-frame', pk=project.id)

    context = {'form':form}
    return render(request, 'managertool/addtask.html', context)

@login_required(login_url='login')
def achieveTask(request, pk):
    task = Task.objects.get(id=pk)
    projectId = task.project.id
    task.checking = True
    task.save()
    return redirect('project-frame', pk=projectId)

@login_required(login_url='login')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    project = task.project
    if request.method == 'POST' :
        task.delete()
        return redirect('project-frame', pk=project.id)
    return render(request, 'managertool/droptask.html', {'task':task})

