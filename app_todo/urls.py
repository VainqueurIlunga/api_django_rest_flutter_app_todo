from django.urls import path,include



from rest_framework.routers import DefaultRouter
from .views import TaskView

router = DefaultRouter()
router.register(r'tasks', TaskView)

urlpatterns = [
  path('', include(router.urls)),
]