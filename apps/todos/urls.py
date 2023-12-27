from django.urls import path

from apps.todos.views import TodosNotCompletedListView, TodosCreateViewSet, TodosDetailView, TodosUpdateView, \
    TodosDeleteView, TodosCompletedListView

urlpatterns = [
    path('not-completed/', TodosNotCompletedListView.as_view(), name='todos-not-completed-list'),
    path('completed/', TodosCompletedListView.as_view(), name='todos-completed-list'),
    path('create/', TodosCreateViewSet.as_view(), name='todos-create'),
    path('detail/<int:pk>/', TodosDetailView.as_view(), name='todos-detail'),
    path('update/<int:pk>/', TodosUpdateView.as_view(), name='todos-update'),
    path('delete/<int:pk>/', TodosDeleteView.as_view(), name='todos-delete'),
]
