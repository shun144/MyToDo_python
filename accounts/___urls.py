# from django.contrib import admin
# from django.urls import include, path
# from . import views

# app_name = 'accounts'
# urlpatterns = [

#   path('', views.signin, name='login'),
  
#   path('signup', views.signup, name='signup'),
  
#   path('password_reset', views.signup, name='password_reset'),
# ]



from django.contrib import admin
from django.urls import include, path

app_name = 'account'
urlpatterns = [
  path('account/', include('allauth.urls')),
]
