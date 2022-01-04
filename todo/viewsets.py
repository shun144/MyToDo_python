from rest_framework import viewsets, filters, mixins
from rest_framework.serializers import Serializer
from .models import Todo, Status
from .serializers import StatusSerializer, TodoSerializer, ListSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response





class TodoViewSet(viewsets.ModelViewSet):
  queryset = Todo.objects.all()
  # queryset = Todo.objects.order_by('-disp_no')
  serializer_class = TodoSerializer






class StatusViewSet(viewsets.ModelViewSet):
  queryset = Status.objects.all()
  serializer_class = StatusSerializer



class ListViewSet(viewsets.ModelViewSet):
  queryset = Status.objects.all()
  serializer_class = ListSerializer


