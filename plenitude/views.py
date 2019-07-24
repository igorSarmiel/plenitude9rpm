from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/login.html', )
    else:
        return render(request, 'registration/login.html', )


def log_out(request):
    logout(request)
    return redirect('/')