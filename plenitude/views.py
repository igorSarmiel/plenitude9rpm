from django.contrib.auth import authenticate, login, logout, get_user
from django.shortcuts import redirect, render
import os
import datetime


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = BASE_DIR + "/logs/log_user.txt"


def log_acessos(user, status):
    now = datetime.datetime.now()
    ano = now.strftime("%Y")
    mes = now.strftime("%m")
    dia = now.strftime("%d")
    horas = now.strftime("%H")
    minutos = now.strftime("%M")
    texto = user +" - "+status +" em "+dia+"/"+mes+"/"+ano+" as "+horas+":"+minutos+" horas"+"\n"
    if os.path.isfile(LOG_PATH):
        with open(LOG_PATH,'a') as log:
            log.write(texto)
            log.close()
    else:
        with open(LOG_PATH,'w') as log:
            log.write(texto)
            log.close()


def listar_acessos(request, usuario):
    lista = []
    with open(LOG_PATH, 'r') as log:
        acessos = log.readlines()
        log.close()
        for acesso in acessos:
            user = acesso.split("-")[0].strip()
            if user == usuario:
                lista.append(acesso)

    return render(request, "registration/lista_acessos.html", {"acessos": lista})



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

if __name__ == "__main__":
    print(BASE_DIR)
    print(LOG_PATH)
    print(os.path.exists(LOG_PATH))