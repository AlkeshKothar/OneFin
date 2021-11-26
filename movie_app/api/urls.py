

from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from movie_app import views 
from rest_framework.routers import DefaultRouter

from .api import RegisterApi,MovieView,CollectionsView

urlpatterns = [
    path('', views.index, name='index'),
    path('register', RegisterApi.as_view()),
    path('login', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('movie',MovieView.as_view(), name='movie'),
    #path('collection',CollectionsView.as_view(), name='collectionmovie'),
   # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

router = DefaultRouter()
router.register(r'collection', CollectionsView, basename='collection')
urlpatterns += router.urls