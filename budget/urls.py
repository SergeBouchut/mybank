from django.conf.urls import include, url

from rest_framework import routers

from .views import CategoryViewSet, TransactionViewSet, base


router = routers.DefaultRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'categories', CategoryViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framwork')),
    url(r'^$', base, name='base'),
]
