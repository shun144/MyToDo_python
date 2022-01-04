from rest_framework import routers
from todo.viewsets import TodoViewSet, StatusViewSet, ListViewSet


router = routers.DefaultRouter()
router.register('todo', TodoViewSet)
router.register('status', StatusViewSet)
router.register('list', ListViewSet)

