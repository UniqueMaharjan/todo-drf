from django.urls import path
from .views import TodoListCreateAPIView, TodoDeleteUpdateRetrieveAPIView

urlpatterns = [
    path('',TodoListCreateAPIView.as_view(), name = "list-create"),
    path('<int:id>/',TodoDeleteUpdateRetrieveAPIView.as_view(), name = "retrieve-del-update")
]