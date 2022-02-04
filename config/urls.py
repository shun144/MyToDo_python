
from django.contrib import admin
from django.urls import include, path
from .routers import router



urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('account.urls')),
    path('', include('account.urls')),
    # path('login/', include('account.urls')),
    path('api/', include(router.urls)),

]

