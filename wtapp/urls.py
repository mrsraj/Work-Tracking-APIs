from django.urls import path
from .views import RegisterUser , LoginUser 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 
from . import views 

urlpatterns = [
    #two new
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    path('register/', RegisterUser .as_view(), name='register_user'), 
    path('login/', LoginUser .as_view(), name='login_user'),
    
    path('tasks/<int:user_id>/<int:grp_id>/', views.get_tasks),
    path('tasks/update/', views.update_tasks),
    path('tasks/add/', views.add_task),
    
    path('task/delete/<int:pk>/', views.deleteTask),
    
    path('addboard/', views.add_Board),
    path('getboard/<int:id>/', views.GetBoard),
]