
import json
from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from account.serializers import UserSerializer

from .form import ManagerSignUpForm, EmployeeSignUpForm
from .models import User
from .controller import LoginController
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

def register(request):
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')


class manager_register(CreateView):
    model = User
    form_class = ManagerSignUpForm
    template_name = 'manager_register.html'
    model.is_manager = True

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = 'employee_register.html'
    model.is_employee = True

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

class admin_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = 'admin_register.html'
    model.is_admin = True

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')




def login_view(request):
    login_controller = LoginController(request)
    ok, context=login_controller.handle_request()
    if ok == 1:
        return redirect('showProductsEmp')
    if ok == 2:
        return redirect('showProductsMng')
    if ok == 3:
        return redirect('adminPage')
    return render(request, 'login.html', context)



@api_view(['GET','POST'])
def add_user(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def view_users(request):
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET','PUT', 'DELETE'])
def detail_user(request, pk):
    try:
        users = User.objects.get(pk = pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        pass
    elif request.method == 'GET':
        serializer = UserSerializer(users)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        pass

def whatsapp_msg(ph, message):
    import time
    import webbrowser as web
    import pyautogui as pg
    Phone = "+40" + ph
    web.open('https://web.whatsapp.com/send?phone='+Phone+'&text='+message)
    time.sleep(15)
    pg.press('enter')

@api_view(['GET','PUT', 'DELETE'])
def update_user(request):
    try:
        id = request.data["id"]
        users = User.objects.get(pk = id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = UserSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            subject = 'Account details changed'
            message = f'Hi {users.first_name}, your account details have been changed\nHere are the new credentials to login:\nusername: {users.username}\npassword: {users.password}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [users.email,]
            send_mail( subject, message, email_from, recipient_list)
            ph = users.phone_number
            whatsapp_msg(ph, message)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        pass
    elif request.method == 'DELETE':
        pass


@api_view(['GET','PUT', 'DELETE'])
def delete_user(request, pk):
    try:
        users = User.objects.get(pk = pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        pass
    elif request.method == 'GET':
        pass
    elif request.method == 'DELETE':
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','POST'])
def login_user(request):
    try:
        username = request.data["username"]
        password = request.data["password"]
        user = User.objects.get(username = username, password = password)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    if request.method == 'GET':
      pass