from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from .views import LogoutView, LogoutAllView, MyTokenObtainPairView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/logout/', LogoutView.as_view(), name='auth_logout'),
    path('api/token/logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
]
