from rest_framework.relations import ManyRelatedField
from .models import Todo, Status
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from django.http import Http404


class StatusSerializer(serializers.ModelSerializer):
  class Meta:
      model = Status
      fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
      model = Todo
      fields = ['task_id', 'disp_no', 'title','description','user_name', 'status']




class ListSerializer(serializers.ModelSerializer):
  tasks = TodoSerializer(many=True)
  class Meta:
      model = Status
      fields = ['id','status', 'tasks']








      




