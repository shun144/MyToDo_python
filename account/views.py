from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate

from .forms import LoginForm, SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from django.contrib.auth import get_user_model

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'account/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'account/login.html'



class SignUp(CreateView):
    """アカウント作成ページ"""
    form_class = SignUpForm
    template_name = 'account/signup.html'

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)


        if form.is_valid():
    
            form.save()
            # username = form.cleaned_data.get('username')
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)

            login(request, user)
            return redirect('/top')

        return render(request, 'account/signup.html', {'form': form})




# def getfnames(models):
#     meta_fields = models._meta.get_fields()
#     # print(meta_fields) 

#     ret = list()
#     for i, meta_field in enumerate(meta_fields):
#         if i > 0:
#             ret.append(meta_field.name)
#     print(ret)