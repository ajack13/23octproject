from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.user.urls')),
    path('email/', include('api.v1.email.urls')),
]
