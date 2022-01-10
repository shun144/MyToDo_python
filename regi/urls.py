from django.urls import include, path
from . import views


app_name = 'regi'

urlpatterns = [

    path('', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),

    path('top/', include('todo.urls'), name='top'),
]   