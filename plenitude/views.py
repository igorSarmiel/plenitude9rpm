from django.contrib.auth import authenticate, login, logout, get_user
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

def password_change(request):
    if request.method == "POST":
        pass1 = request.POST["password1"]
        pass2 = request.POST["password2"]
        if pass1 == pass2:
            user = get_user(request)
            user.set_password(pass1)
            user.save()
            return redirect('home')
        else:
            return render(request, "registration/password_change_form.html",{"msn":"As senhas não conferem. Tente de novo."} )
    else:
        return render(request, "registration/password_change_form.html",)