from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response

from apps.todos.models import Todos
from apps.todos.serializers import TodosSerializer, TodosCreateSerializer, TodosRetrieveSerializer, \
    TodosUpdateSerializer
from apps.users.permissions import UserPermission


class TodosNotCompletedListView(ListAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
    permission_classes = [UserPermission]

    def get_queryset(self):
        return Todos.objects.filter(user_id=self.request.user, is_completed=False)


class TodosCompletedListView(ListAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
    permission_classes = [UserPermission]

    def get_queryset(self):
        return Todos.objects.filter(user_id=self.request.user, is_completed=True)


class TodosCreateViewSet(CreateAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosCreateSerializer
    permission_classes = [UserPermission]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class TodosDetailView(RetrieveAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosRetrieveSerializer
    permission_classes = [UserPermission]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.user_id or request.user.is_staff:
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=200)
        else:
            return Response({"detail": "You do not have permission to access this todo."}, status=403)


class TodosDeleteView(DestroyAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
    permission_classes = [UserPermission]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.user_id or request.user.is_staff:
            instance.delete()
            return Response({"detail": "Message successfully deleted."}, status=200)
        else:
            return Response({"detail": "You do not have permission to delete this todo."}, status=403)


class TodosUpdateView(UpdateAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosUpdateSerializer
    permission_classes = [UserPermission]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if request.user == instance.user_id:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return Response({"detail": "You do not have permission to update this todo."}, status=403)
