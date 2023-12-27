from django.urls import path, include

urlpatterns = [
    path('', include("apps.core.urls")),
    path('users/', include("apps.users.urls")),
    path('todos/', include("apps.todos.urls")),
]
