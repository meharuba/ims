from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.shortcuts import render

def profile(request):
    return render(request, 'profile.html')

# class MyLoginView(LoginView):
#     template_name = 'login.html'

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('example')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


