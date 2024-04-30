from django.urls import include, path

# import routers
from rest_framework import routers 
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
# import everything from views
from .views import *
  
# define the router
router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet)
router.register(r'student', StudentViewSet)



  
# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    #path('api-token-auth/', views.obtain_auth_token)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) # this line is used for only login & logout feature in DRF window
]