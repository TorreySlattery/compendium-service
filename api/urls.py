from django.urls import include, path
from django.conf.urls import url

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

import api.views


schema_view = get_schema_view(
   openapi.Info(
      title="Compendium API",
      default_version='v1',
      description="The compendium service API"
   )
)

router = DefaultRouter()
router.register(r'spells', api.views.SpellViewSet)

api_v1_urlpatterns = [
    path('', include(router.urls))
]

urlpatterns = [
   url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + api_v1_urlpatterns
