from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.views import View

class LoginView(View):
    def post(self, request):
        username = request.POST.get('l')
        password = request.POST.get('p')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/blog/')
        else:
            return redirect('/')
    def get(self, request):
        return render(request, 'login.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class RegisterView(View):
    def post(self, request):
        a = User.objects.create(
            username=request.POST.get('l'),
            password=request.POST.get('p')
        )
        return redirect('/')
    def get(self, request):
        return render(request, 'register.html')

class BlogView(View):
    def get(self, request):
        data = {
            "blog": Maqola.objects.filter(muallif__user=request.user),
            "muallif": Muallif.objects.get(user=request.user)
        }
        return render(request, 'blog.html', data)

class MaqolaView(View):
    def get(self, request, id):
        data = {
            "maqola": Maqola.objects.get(muallif__user=request.user, id=id)
        }
        return render(request, "maqola.html", data)

class MaqolaAddView(View):
    def get(self, request):
        return render(request, 'maqola_add.html')
    def post(self, request):
        if request.user.is_authenticated:
            Maqola.objects.create(
                sarlavha = request.POST.get('s'),
                mavzu = request.POST.get('m'),
                matn = request.POST.get('mn'),
                muallif = Muallif.objects.get(user=request.user),
            )
            return redirect('/blog/')