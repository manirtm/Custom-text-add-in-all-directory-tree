from django.shortcuts import render, redirect
import os
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            messages.success(request, "Account was created for" + user)
            return redirect('login')
    return render(request, 'register.html', {"form":form})

def loginPage(request):
    if request.POST:
        form = request.POST
        username = form['username']
        password = form['password']
        request.session['username'] = username
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            login(request, user)
            return redirect('customtext/')
        else:
            messages.info(request, "Username or Password is incorrect")
            return render(request, 'login.html')
    return render(request, 'login.html')

def logOutUser(request):
    del request.session['username']
    logout(request)
    return redirect('login')

def text_add(request):
    if request.POST:
        form = request.POST
        text_area = form.get('add_text')
        file_location = os.path.join(os.path.abspath(os.path.dirname(__file__)),'Text_Files/')
        if text_area is not None:
            for root, dirs, files in os.walk(file_location):
                for file_ in files:
                    file_path = os.path.join(root, file_)
                    data = open(file_path, 'a')
                    data.write(text_area+'\n')
                    data.close()
            return render(request, 'success.html',{"root":root})

    return render(request, 'home.html')

