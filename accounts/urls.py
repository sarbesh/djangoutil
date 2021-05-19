from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as auth_view
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', auth_view.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]