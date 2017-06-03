from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render

@login_required
def index(request):
    return redirect('/clinic')


def user_login(request):
    if request.method== 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponse("valide login details suplied.")
            else:
                return HttpResponse("Votre compte est désactivé")
        else:
            print("Invalide login details ({0} or {1} .".format(username , password))
            return HttpResponse("invalide login details suplied.")
    else:
        return render(request, 'registration/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')