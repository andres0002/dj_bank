# django
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
# third
# own
from apps.user.models import Cliente

# Create your views here.

class Login(View):
    template_name = 'login.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("signin_username")
        password = request.POST.get("signin_password")
        usuario = auth.authenticate(username=username, password=password)

        if usuario != None and usuario.is_active:
            auth.login(request, usuario)
            cliente = Cliente.objects.filter(usuid=usuario.pk)

            if cliente[0].rol == "CLI":
                return HttpResponseRedirect(reverse('user:client:perfil_cliente'))

            elif cliente[0].rol == "AMD":
                return HttpResponseRedirect(reverse('user:admin:perfil_administrador'))

            else:
                messages.add_message(request, messages.ERROR, "Rol de usuario inexistente")

        else:
            if usuario == None:
                messages.add_message(request, messages.ERROR, "El Usuario no existe en el Sistema")

            else:
                messages.add_message(request, messages.ERROR, "El Usuario esta inactivo")

        return render(request, self.template_name)

class Logout(View):

    def get(self, request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('login'))