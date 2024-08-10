from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).first()

        if user:
            request.session['user_id'] = user.id
            messages.success(request, 'login successful.')
            return redirect('dashboard')

        else :
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create(username=username, password=password)
        messages.success(request, 'Registration successful. please login')
        return redirect('login')
    
    return render (request, 'register.html')


def dashboard(request):
    user_id = request.session.get('user_id')
    if user_id:
        return render(request, 'dashboard.html', {'user_id': user_id})       
    else:
        messages.error(request, 'You are not logged in.')
        return redirect('login')
    
def logout(request):
    request.session.clear()
    messages.success(request, 'Logout successful.')
    return redirect('login')