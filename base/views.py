from rest_framework import generics
from api.mixins import UserQuerySetMixin,UserOwnerMixin
from base.serializers import TodoSerializer
from base.models import Todo


class TodoListCreateAPIView(UserQuerySetMixin,generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        body = serializer.validated_data.get('body')
        if body is None:
            body = title
        return serializer.save(creator = self.request.user, body = body)
    

class TodoDeleteUpdateRetrieveAPIView(UserQuerySetMixin,UserOwnerMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.body:
            instance.body = instance.title

