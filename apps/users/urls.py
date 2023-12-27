from django.urls import path
from .views import UserCreateViewSet, UserDetailView, UserDeleteViewSet

urlpatterns = [
    path('create/', UserCreateViewSet.as_view(), name='user-create'),
    path('detail/', UserDetailView.as_view(), name='user-detail'),
    path('delete/', UserDeleteViewSet.as_view(), name='user-delete')
]
