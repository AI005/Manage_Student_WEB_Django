from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# Create your views here.

class ClassLogin(View):
    def get(self, request):
        return render(request, 'Login/login.html')
    def post(self, request):
        uname = request.POST.get('Username')
        pword = request.POST.get('Password')
        my_user = authenticate(username=uname, password=pword)
        if my_user is None:
            return HttpResponse("khong tao dc tai khoan.")
        login(request, my_user)
        return render(request, 'Login/student.html')