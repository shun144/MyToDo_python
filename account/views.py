from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate

from .forms import LoginForm
from django.contrib.auth.views import LoginView, LogoutView


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'account/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'account/home.html'