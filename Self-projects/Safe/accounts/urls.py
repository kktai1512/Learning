from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'accounts', views.AccountViewSet)
router.register(r'transactions', views.TransactionViewSet)
router.register(r'tags', views.TransactionTagViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    #this is for the login logout view
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]