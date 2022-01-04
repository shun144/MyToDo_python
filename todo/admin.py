from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import Todo, Activate
from app.models import User

# Register your models here.

class TodoAdmin(admin.ModelAdmin):

    fields = ['todo_title', 'memo', 'datetime', 'tags']

    list_display = ('todo_title', 'datetime', 'created_at', 'tag_list')
    list_display_links = ('todo_title', 'datetime','tag_list')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    pass

admin.site.register(Todo,TodoAdmin)
admin.site.register(Activate)