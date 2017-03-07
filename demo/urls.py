from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import DataViewSet

router = DefaultRouter()
router.register('data', DataViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
