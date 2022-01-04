
from django.contrib import admin
from django.urls import include, path
from .routers import router
from django.views.generic import TemplateView # 追加
# from ..todo.views import TodoDetailAPIView

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('accounts.urls')),
    path('todo/', include('todo.urls')),
    path('accounts/', include('accounts.urls')),

    path('api/', include(router.urls)),
    # path('todo/test', TemplateView.as_view(template_name='todo_list.html'))
    
]
