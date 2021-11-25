

from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from movie_app import views
from .api import RegisterApi, EmployeeCreateApi,EmployeeApi,EmployeeUpdateApi,EmployeeDeleteApi

urlpatterns = [
    path('', views.index, name='index'),
    path('register', RegisterApi.as_view()),
    path('login', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),

    #protected
    path('create',EmployeeCreateApi.as_view()),

    path('<int:pk>',EmployeeUpdateApi.as_view()),
    path('<int:pk>/delete',EmployeeDeleteApi.as_view()),
   # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]