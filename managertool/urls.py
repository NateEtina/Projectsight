
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('signup/', views.signupUser, name='sign-up'),
    path('projectframe/<str:pk>', views.projectFrame, name='project-frame'),
    path('addproject/', views.addProject, name='add-project'),
    path('updateproject/<str:pk>', views.updateProject, name='update-project'),
    path('deleteproject/<str:pk>', views.deleteProject, name='delete-project'),

    path('projecframe/<str:pk>/addtask', views.addTask, name='add-task'),
    path('check-task/<str:pk>', views.achieveTask, name='check-task'),
    path('updatetask/<str:pk>', views.updateTask, name='update-task'),
    path('deletetask/<str:pk>', views.deleteTask, name='delete-task'),
]