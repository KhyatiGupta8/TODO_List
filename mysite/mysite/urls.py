"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage,name='todopage1'),
    path('index',views.index,name='index'),
    path('add',views.addtodo,name='add'),
    path('complete/<todo_id>',views.completetodo,name='complete'),
    path('deleteCompleted',views.deleteCompleted,name='deleteCompleted'),
    path('deleteAll',views.deleteAll,name='deleteall'),
    path('delete/<todo_id>', views.deletetodo, name='delete'),
    
    path('login',views.login_request,name='login'),
    path('logout',views.logout_request,name='logout'),

]
