from django.contrib.auth import authenticate, login, logout, get_user
from django.shortcuts import redirect, render
import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = BASE_DIR+"/logs/log_user.txt"

def log_acessos(user, status):
    now = datetime.datetime.now()
    ano = now.strftime("%Y")
    mes = now.strftime("%m")
    dia = now.strftime("%d")
    horas = now.strftime("%H")
    minutos = now.strftime("%M")
    texto = user +" - "+status +" em "+dia+"/"+mes+"/"+ano+" as "+horas+":"+minutos+" horas"+"\n"
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH,'a', encoding='utf8') as log:
            log.write(texto)
            log.close()
    else:
        with open(LOG_PATH,'w', encoding='utf8') as log:
            log.write(texto)
            log.close()

def listar_acessos(request, usuario):
    with open(LOG_PATH, 'r', encoding="utf8") as log:
        acessos = log.readlines()
        log.close()
    return render(request, "registration/lista_acessos.html",{"acessos":acessos})



def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            log_acessos(username, "Acessou")
            return redirect('home')
        else:
            return render(request, 'registration/login.html', )
    else:
        return render(request, 'registration/login.html', )


def log_out(request):
    log_acessos(request.user.username, "Saiu")
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
            log_acessos(request.user.username, "Mudou a senha")
            return redirect('home')
        else:
            return render(request, "registration/password_change_form.html",{"msn":"As senhas não conferem. Tente de novo."} )
    else:
        return render(request, "registration/password_change_form.html",)