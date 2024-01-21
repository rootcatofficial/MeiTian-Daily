from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreateUserForm, LoginForm, CreateTaskForm, UpdateUserForm

from django.contrib.auth.models import auth # For Login and Logout
from django.contrib.auth import authenticate, login # For user authentication

from django.contrib.auth.decorators import login_required

from .models import Task, User, Profile

# - import Django messages for messages

from django.contrib import messages


# Create your "views" here. The pages our routes responds with

# These are VIEWS

    # - For HOME page 
def home(requests):

    return render(requests, 'index.html',)

    # - For Reistering  / Creating a User Page
def Register(requests):
    
    form = CreateUserForm()

    if requests.method == 'POST':
        form =  CreateUserForm(requests.POST)

        if form.is_valid():

            current_user = form.save(commit=False)

            form.save()

            profile = Profile.objects.create(user=current_user)

            messages.success(requests, "User registration was successful!")

            return redirect('login')

    context = {'form':form}

    return render(requests, 'register.html', context=context)


    # - For Login  / Authenticating a User Page
def LoginPage(requests):
    
    form = LoginForm()

    if requests.method == 'POST':
        form =  LoginForm(requests, data=requests.POST)

        if form.is_valid():
            username = requests.POST.get('username')
            password = requests.POST.get('password')

            user = authenticate(requests, username=username, password=password)

            if user is not None: # (i.e if the user exists)
                auth.login(requests, user) # authenticate (login) the user


                return redirect("dashboard" )

    context = {'form':form}

    return render(requests, 'login.html', context=context)



    # - for Dashboard page
@login_required(login_url='login') #login validator before accessing the dashboard page
def Dashboard(requests):

    profile_pic = Profile.objects.get(user=requests.user)

    context = {'profile': profile_pic}


    return render(requests, 'profile/dashboard.html', context=context)




    # - for Profile Management
@login_required(login_url='login') #login validator before accessing the dashboard page
def Profile_Management(requests):

    if requests.method == 'POST':

        user_form = UpdateUserForm(requests.POST, instance=requests.user)

        if user_form.is_valid():
            
            user_form.save()

            return redirect('dashboard')

    user_form = UpdateUserForm(instance=requests.user) # this is showing our user form and content before update

    context = {'user_form': user_form}

    return render(requests, 'profile/profile-management.html', context=context)


    # - for Deleting Account
@login_required(login_url='login') #login validator before accessing the dashboard page
def DeleteAccount(requests):

    if requests.method == 'POST':

        deleteuser = User.objects.get(username=requests.user)

        deleteuser.delete()

        return redirect('')


    return render(requests, 'profile/delete-account.html')




    pass



    # - for CREATE page
@login_required(login_url='login') #login validator before accessing the dashboard page
def Create(requests):

    form = CreateTaskForm()

    if requests.method == 'POST':
        form = CreateTaskForm(requests.POST)

        if form.is_valid():
            task = form.save(commit=False)

            task.user = requests.user

            task.save()

            return redirect('read')

    context = {'form': form}

    return render(requests, 'profile/create.html', context=context)


    # - for Read page
@login_required(login_url='login') #login validator before accessing the dashboard page
def Read(requests):

    current_user = requests.user.id

    task = Task.objects.all().filter(user=current_user)

    context = {'task':task}

    return render(requests, 'profile/read.html', context=context)

 
    # - for Update page
@login_required(login_url='login') #login validator before accessing the dashboard page
def Update(requests, pk):

    task = Task.objects.get(id=pk)

    form = CreateTaskForm(instance=task)

    if requests.method == 'POST':

        form = CreateTaskForm(requests.POST, instance=task)

        if form.is_valid():
            
            form.save()

            return redirect('read')

    context = {'form':form}

    return render(requests, 'profile/update.html', context=context)



# - for Delete page
@login_required(login_url='login') #login validator before accessing the dashboard page
def Delete(requests, pk):

    task = Task.objects.get(id=pk)

    if requests.method == 'POST':

        task.delete()

        return redirect('read')

    return render(requests, 'profile/delete.html')




    


   # - For Login  / Authenticating a User Page
def Logout(requests):
    
    auth.logout(requests)

    return redirect("")