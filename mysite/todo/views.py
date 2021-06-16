from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.views.decorators.http import require_POST


@login_required
def logout_request(request):
	logout(request)
	return render(request,'todo/login.html')
def login_request(request):
	if not request.user.is_authenticated:
		context = {}
	else:
		todo_list = Todo.objects.filter(user_username_contains=request.user)
		form = AuthenticationForm()
		if request.method=="POST":

			form= AuthenticationForm(request.POST)
			if form.is_valid():
				user = form.save(using=self._db,commit=True)
				username=form.cleaned_data.get('username')
				password=form.cleaned_data.get('username')
				user=authenticate(usernname=username,password=password)
				user.save();

				if request.user.is_authenticated(username,password):
					login(request,user)
					messages.info(request,f"You are now logged in as {username}")
					return redirect('index')
				else:
					messages.error(request,'Invalid username or password')
			else:
					messages.error(request,'Invalid username or password')
		form =AuthenticationForm()
		todo_list = Todo.objects.filter(user=request.user)
		context = {'todo_list':todo_list,'form':form}
	return render(request,'todo/home.html',context)

def homepage(request):
	return render(request,'todo/login.html',{})

def index(request):
	todo_list = Todo.objects.order_by('-created_date')
	form = TodoForm()
	context={'todo_list':todo_list, 'form': form}
	return render(request,'todo/home.html',context)

@require_POST
def addtodo(request):
	form = TodoForm(request.POST)
	#print(request.POST['text'])
	if form.is_valid():
		new_todo=Todo(text=request.POST['text'])
		new_todo.save()
	return redirect('index')
def deletetodo(request, todo_id):
    todo = Todo.objects.filter(pk=todo_id)
    todo.delete()
    return redirect('index')
def completetodo(request,todo_id):
	todo=Todo.objects.get(pk=todo_id)
	todo.complete=True
	todo.save()
	return redirect('index')
def deleteCompleted(request):
	Todo.objects.filter(complete__exact=True).delete()
	redirect('index')
	return HttpResponseRedirect(reverse('index'))
def deleteAll(request):
	Todo.objects.all().delete()
	redirect('index')
	return HttpResponseRedirect(reverse('index'))

