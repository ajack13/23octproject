from django.conf import settings
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Interview API Docs",
        default_version='v1'
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('v1/', include('api.v1.urls'))
]

if settings.DEBUG:
    docs = [path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), ]
    urlpatterns = urlpatterns + docs
