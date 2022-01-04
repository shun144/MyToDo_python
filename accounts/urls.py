from django.contrib import admin
from django.urls import include, path

# app_name = 'account'
urlpatterns = [
  path('', include('allauth.urls')),
]


# from django.urls import include, path
# from django.contrib.auth import views as auth_views

# app_name = 'accounts'
# urlpatterns = [
#   path('login/', auth_views.LoginView.as_view(template_name='account/login.html')),
# ]
